import KoaApp from 'koa'
import _ from 'koa-route'
import mongoose from 'mongoose'

import TestHandler from '~/api/handlers/test'
import HealthcheckHandler from '~/api/handlers/healthcheck'

export default class CosmosApp {
  constructor(config) {
    this.config = config
    this.allowedMethods = ['get', 'post', 'put', 'delete']
    this.app = new KoaApp()

    this.configureMiddleware()
    this.handlers = [
      new TestHandler(this),
      new HealthcheckHandler(this),
    ]
  }

  configureMiddleware() {
    this.app.use(async function (ctx, next) {
      const start = new Date()
      await next()
      const ms = new Date() - start
      ctx.set('X-Response-Time', `${ms}ms`)
    })
  }

  async initializeServices() {
    await this.initializeMongoDB()
  }

  async initializeMongoDB() {
    const hosts = this.config.get('app.services.mongo.hosts')
    this.app.context.mongodb = mongoose.createConnection(hosts)
    this.app.context.mongodb.on('error', console.error)
    try {
      const result = await this.app.context.mongodb.db.admin().ping()
      if (!result) {
        console.log('FAILED TO CONNECT TO MONGO!')
      }
    } catch (err) {
      console.log(err)
    }
  }

  async run() {
    await this.initializeServices()
    this.handlers.forEach((handler) => {
      this.allowedMethods.forEach((methodName) => {
        if (!handler[methodName]) {
          return
        }

        const handlerMethod = handler[methodName].bind(handler)
        const method = _[methodName]
        this.app.use(
          method(handler.route, async (ctx) => {
            await handlerMethod(ctx)
          })
        )
      })
    })

    this.app.listen(3000)
  }
}
