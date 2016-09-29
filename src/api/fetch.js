import fetch from 'node-fetch'

export default async function (url) {
  try {
    const res = await fetch(url)
    const json = await res.json()
    return json
  } catch (e) {
    console.log("Error!", e)
    return null
  }
}
