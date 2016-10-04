import config from 'config'
import CosmosApp from '~/api/app'

const command = 'start'
const describe = 'starts the cosmos API'
const builder = () => {
}
const handler = function () {
  const app = new CosmosApp(config)
  app.run()
}

export default {
  command,
  describe,
  builder,
  handler,
}
