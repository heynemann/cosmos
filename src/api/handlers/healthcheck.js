import checkMongoDb from '~/extensions/healthcheck/mongodb'

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
    let failed = false
    this.services.mongo = await checkMongoDb(ctx.mongodb)

    ctx.body = this.services
    if (this.hasFailed()) {
      ctx.status = 500
    }
  }
}
