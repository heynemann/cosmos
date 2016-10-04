import mongoose from 'mongoose'

export async function check(mongodb) {
  const result = {
    up: false,
    error: null,
    uptime: null,
    localTime: null,
    connections: null,
  }

  try {
    const res = await mongodb.db.admin().serverStatus()
    if (res) {
      result.up = true
      result.uptime = res.uptime
      result.localTime = res.localTime
      result.connections = res.connections
    } else {
      result.error = 'Could not get server status!'
    }
  } catch (error) {
    result.error = error.message
  }

  return result
}

export async function connect(hosts) {
  const mongodb = mongoose.createConnection(hosts)
  mongodb.on('error', (err) => {
    throw err
  })
  const result = await mongodb.db.admin().serverStatus()
  if (!result) {
    throw new Error('Failed to get server status from mongodb.')
  }

  return mongodb
}
