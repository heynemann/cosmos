import { check as checkMongoDb } from '~/extensions/mongodb'

export default class HealthcheckHandler {
  constructor(app) {
    this.app = app
    this.route = '/healthcheck'
    this.resetServices()
  }

  resetServices() {
    this.services = {}
  }

  hasFailed() {
    return (
      !this.services.mongo.up
    )
  }

  async get(ctx) {
    this.services.mongo = await checkMongoDb(ctx.mongodb)
    ctx.body = JSON.stringify(this.services)

    if (this.hasFailed()) {
      ctx.status = 500
    }
  }
}
