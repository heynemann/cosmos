import chaiMod from 'chai'

const initializeChai = () => {
  chaiMod.config.includeStack = true // turn on stack trace
}

const initializeTests = () => {
  process.env.NODE_ENV = 'test'

  initializeChai()
}

export const expect = chaiMod.expect
export const chai = chaiMod

initializeTests()
