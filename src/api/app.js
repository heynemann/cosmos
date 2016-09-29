import KoaApp from 'koa'
import _ from 'koa-route'
import TestHandler from './handlers/test'

export default class CosmosApp {
  constructor() {
    this.allowedMethods = ['get', 'post', 'put', 'delete']
    this.app = new KoaApp()
    this.handlers = [
      new TestHandler(this),
    ]
  }

  async run() {
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
