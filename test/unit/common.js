import config from 'config'
import * as sap from 'supertest-as-promised'

// Common import must come before all other app imports to set node env
import { expect as exp, chai as chaiMod } from '../common'

import CosmosApp from '../../src/api/app'


export const expect = exp
export const chai = chaiMod

let app = null

// Before each test create and destroy the app if it does not exist
beforeEach(async function () {
  if (!app) {
    app = new CosmosApp(config)
    await app.initializeApp()
  }

  this.app = app
  // From http://stackoverflow.com/questions/33369389/how-can-i-use-es2016-es7-async-await-in-my-acceptance-tests-for-a-koa-js-app
  this.request = sap.agent(this.app.app.listen())
})
