import config from 'config'
import test from 'ava'
import * as sap from 'supertest-as-promised'

import CosmosApp from '../../../../src/api/app'

// import { expect } from '../../common'

// describe('Handlers', () => {
  // describe('Healthcheck Handler', () => {
    // it('should return 200 if all services up', async function () {
      // const res = await this.request.get('/healthcheck')
      // expect(res.status).to.equal(200)

      // const body = res.text
      // expect(body).not.to.equal('')

      // const result = JSON.parse(body)

      // expect(result.mongo).not.to.equal(null)
      // expect(result.mongo.up).to.equal(true)
    // })
  // })
// })

let app = null
test.before(async () => {
  app = new CosmosApp(config)
  await app.initializeApp()
})

test.beforeEach(async (t) => {
  t.context.app = app
  // From http://stackoverflow.com/questions/33369389/how-can-i-use-es2016-es7-async-await-in-my-acceptance-tests-for-a-koa-js-app
  t.context.request = sap.agent(app.app.listen())
})

test('Healthcheck should return 200 if all services are up', async (t) => {
  const res = await t.context.request.get('/healthcheck')
  t.is(res.status, 200)

  const body = res.text
  t.not(body, '')

  const result = JSON.parse(body)

  t.not(result.mongo, null)
  t.truthy(result.mongo.up)
})
