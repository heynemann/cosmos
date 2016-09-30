import getURL from '../fetch'

export default class TestHandler {
  constructor(app) {
    this.app = app
    this.route = '/test'
    this.url = 'https://api.github.com/orgs/facebook'
  }

  async get(ctx) {
    //ctx.body = await getURL(this.url)
    ctx.body = await this.app.mongodb.db.admin().ping()
  }
}
