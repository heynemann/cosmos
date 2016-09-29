import koaApp from 'koa'
import fetch from 'node-fetch'

export class CosmosApp {
    constructor() {
        this.app = new koaApp()
    }

    async get() {
        try {
            const res = await fetch('https://api.github.com/orgs/facebook');
            const json = await res.json();
            return json
        } catch (e) {
            console.log(e)
        }
    }

    async run() {
        const self = this
        this.app.use(async ctx => {
          ctx.body = await self.get()
        });
        this.app.listen(3000)
    }
}
