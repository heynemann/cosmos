export default async function check(mongodb) {
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
      result.error = "Could not get server status!"
    }
  } catch (error) {
    result.error = error.message
  }

  return result
}
