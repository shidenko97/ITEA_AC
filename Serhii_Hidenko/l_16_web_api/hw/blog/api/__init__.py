from flask import Blueprint
from flask_restplus import Api

from blog.api.views import api as posts_ns
from blog.api.views import api_tags as tags_ns


api_bp = Blueprint("api", __name__)
api = Api(
    api_bp,
    version="1.0",
    title="Cool blog REST API",
    description="My simple API for small blog"
)
api.add_namespace(posts_ns)
api.add_namespace(tags_ns)
