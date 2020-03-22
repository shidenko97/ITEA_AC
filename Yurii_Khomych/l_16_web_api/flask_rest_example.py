from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        if todo_id in todo_id:
            return {todo_id: todos[todo_id]}
        return {}

    def put(self, todo_id):
        todos[todo_id] = request.form["todos"]
        return {todo_id: todos[todo_id]}


api.add_resource(TodoSimple, "/<string:todo_id>")

if __name__ == "__main__":
    app.run(debug=True)
