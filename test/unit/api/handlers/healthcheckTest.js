import { expect } from '../../common'

describe('Handlers', () => {
  describe('Healthcheck Handler', () => {
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
})
