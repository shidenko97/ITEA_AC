from aiohttp import web


async def handle(request):
    name = request.match_info.get("your_name", "Anonymous")
    text = "Hello, " + name
    return web.json_response({"text": text})


app = web.Application()
app.add_routes([web.get("/", handle), web.get("/{your_name}", handle)])

if __name__ == "__main__":
    web.run_app(app,)
