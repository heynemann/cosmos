import KoaApp from 'koa'
import fetch from 'node-fetch'

export default class CosmosApp {
  constructor() {
    this.app = new KoaApp()
    this.url = 'https://api.github.com/orgs/facebook'
  }

  async get() {
    try {
      const res = await fetch(this.url)
      const json = await res.json()
      return json
    } catch (e) {
      return null
    }
  }

  async run() {
    const self = this

    this.app.use(async (ctx) => {
      ctx.body = await self.get()
    })

    this.app.listen(3000)
  }
}
