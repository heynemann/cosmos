export default class TestHandler {
  constructor(app) {
    this.app = app
    this.route = '/healthcheck'
    this.resetServices()
  }

  resetServices() {
    this.services = {
      mongo: {
        up: true,
        uptime: 0,
        localTime: null,
        connections: {},
        error: null,
      }
    }
  }

  async get(ctx) {
    let failed = false
    try {
      const res = await ctx.mongodb.db.admin().serverStatus()
      if (res) {
        this.services.mongo.uptime = res.uptime
        this.services.mongo.localTime = res.localTime
        this.services.mongo.connections = res.connections
      } else {
        this.services.mongo.up = false
        this.services.mongo.error = "Could not get server status!"
        failed = true
      }
    } catch (error) {
      this.services.mongo.up = false
      this.services.mongo.error = error.message
      failed = true
    }

    ctx.body = this.services
    if (failed) {
      ctx.status = 500
    }
  }
}
