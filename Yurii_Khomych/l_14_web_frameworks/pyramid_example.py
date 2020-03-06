from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    # return "Hello"
    return Response("Hello World!")


def hello_friend(request):
    return Response("Hello Friend!")


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_route("friend", "/friend")
        config.add_view(hello_world, route_name="hello")
        config.add_view(hello_friend, route_name="friend")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()
