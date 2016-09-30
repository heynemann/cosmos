import yargs from 'yargs'
import pjson from '../package.json'

const startCmd = require('./cmd/start')

export default yargs
  .usage('Cosmos is responsible for creating your own Data Universe.')
  .demand(1)
  .showHelpOnFail(true, 'Specify --help for available options')
  .command(startCmd)
  .help()
  .version(() => pjson.version)
  .strict()
  .argv
