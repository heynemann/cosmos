import * as sap from 'supertest-as-promised'
import config from 'config'

import CosmosApp from '../../src/api/app'
import { expect as exp, chai as chaiMod } from '../common'


const initializeTests = () => {
}

export const expect = exp
export const chai = chaiMod

initializeTests()

beforeEach(async function () {
  this.app = new CosmosApp(config)
  await this.app.initializeApp()

  // From http://stackoverflow.com/questions/33369389/how-can-i-use-es2016-es7-async-await-in-my-acceptance-tests-for-a-koa-js-app
  this.request = sap.agent(this.app.app.listen())
})
