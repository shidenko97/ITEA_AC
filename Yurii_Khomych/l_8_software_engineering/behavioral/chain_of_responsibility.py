class HttpHandler:
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    def handle(self, code):
        if code == 404:
            return "Page not found"


class Http500Handler(HttpHandler):
    def handle(self, code):
        if code == 500:
            return "Server error"


class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, handler_):
        self._handlers.append(handler_)

    def response(self, code):
        for handler_ in self._handlers:
            msg = handler_.handle(code)
            if msg:
                print("Response: %s" % msg)
                break
        else:
            print("Incorrect code")


client = Client()
client.add_handler(Http404Handler())
client.add_handler(Http500Handler())
client.response(400)
client.response(404)
client.response(500)
