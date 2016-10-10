//import config from 'config'
//import test from 'ava'
//import * as sap from 'supertest-as-promised'

//import CosmosApp from '../../../../src/api/app'

import { expect } from '../../common'

describe('Commands', () => {
  beforeEach(function () {
    const self = this
    this.prevExit = process.exit
    process.exit = () => { self.exit = true }
  })

  afterEach(function () {
    process.exit = this.prevExit
  })

  describe('Version Command', () => {
    it.only('should return current version', async () => {
      process.argv = ['cosmos --version']
      const rootCmd = require('../../../src/cmd')
      console.log('result', rootCmd)
    })
  })
})

//let app = null
//test.before(async () => {
  //app = new CosmosApp(config)
  //await app.initializeApp()
//})

//test.beforeEach(async (t) => {
  //t.context.app = app
  //// From http://stackoverflow.com/questions/33369389/how-can-i-use-es2016-es7-async-await-in-my-acceptance-tests-for-a-koa-js-app
  //t.context.request = sap.agent(app.app.listen())
//})

//test('Healthcheck should return 200 if all services are up', async (t) => {
  //const res = await t.context.request.get('/healthcheck')
  //t.is(res.status, 200)

  //const body = res.text
  //t.not(body, '')

  //const result = JSON.parse(body)

  //t.not(result.mongo, null)
  //t.truthy(result.mongo.up)
//})
