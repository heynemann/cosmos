import KoaApp from 'koa'
import _ from 'koa-route'

import HealthcheckHandler from '~/api/handlers/healthcheck'
import { connect as connectMongoDb } from '~/extensions/mongodb'

export default class CosmosApp {
  constructor(config) {
    this.config = config
    this.allowedMethods = ['get', 'post', 'put', 'delete']
    this.app = new KoaApp()

    this.configureMiddleware()
    this.handlers = [
      new HealthcheckHandler(this),
    ]
  }

  configureMiddleware() {
    this.app.use(async (ctx, next) => {
      const start = new Date()
      await next()
      const ms = new Date() - start
      ctx.set('X-Response-Time', `${ms}ms`)
    })
  }

  async initializeServices() {
    const hosts = this.config.get('app.services.mongo.hosts')
    this.app.context.mongodb = await connectMongoDb(hosts)
  }

  async initializeApp() {
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
  }

  async run() {
    await this.initializeApp()
    this.app.listen(3000)
  }
}
