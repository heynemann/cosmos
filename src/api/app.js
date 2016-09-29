import KoaApp from 'koa'
import _ from 'koa-route'
import getURL from './fetch'

export default class CosmosApp {
  constructor() {
    this.app = new KoaApp()
    this.url = 'https://api.github.com/orgs/facebook'
    this.handlers = [
      { method: 'GET', route: '/test', handler: this.handleTest },
    ]
  }

  async handleTest(ctx) {
    ctx.body = await getURL(this.url)
  }

  async run() {
    const self = this
    this.handlers.forEach((route) => {
      const handler = route.handler.bind(self)
      const method = _[route.method.toLowerCase()]
      self.app.use(
        method(route.route, async (ctx) => {
          await handler(ctx)
        })
      )
    })

    this.app.listen(3000)
  }
}
