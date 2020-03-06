import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class JonnyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Jonny")


def make_app():
    return tornado.web.Application(
        [(r"/", MainHandler), (r"/jonny", JonnyHandler),]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
