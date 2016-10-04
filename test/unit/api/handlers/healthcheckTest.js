import * as sap from 'supertest-as-promised'
import config from 'config'

import CosmosApp from '../../../../src/api/app'
import { expect } from '../../common'

describe('Healthcheck Handler', () => {
  beforeEach(async function () {
    this.app = new CosmosApp(config)
    await this.app.initializeApp()
    this.request = sap.agent(this.app.app.listen())
  })

  it('should return 200 if all services up', async function () {
    const res = await this.request.get('/healthcheck')
    expect(res.status).to.equal(200)

    const body = res.text
    expect(body).not.to.equal('')

    const result = JSON.parse(body)
    expect(result.mongo).not.to.equal(null)
    expect(result.mongo.up).to.equal(true)
  })
})
