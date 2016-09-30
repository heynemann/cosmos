import config from 'config'
import CosmosApp from '../api/app'

export const command = 'start'
export const describe = 'starts the cosmos API'
export const builder = () => {
}
export const handler = function () {
  const app = new CosmosApp(config)
  app.run()
}
