from flask import request
from sqlalchemy.orm.exc import NoResultFound

from blog.api.utils import (get_all_posts, create_post, get_post, delete_post,
                       change_post, get_all_tags, create_tag, get_tag,
                       delete_tag, change_tag)
from flask_restplus import fields, Resource, Namespace


api = Namespace("Posts", description="Post management", path="/posts")
api_tags = Namespace("Tags", description="Tag management", path="/tags")

tag_model = api_tags.model("Tag", {
    "id": fields.Integer(readonly=True, description="ID of tag"),
    "name": fields.String(required=True, description="Title of tag"),
    "slug": fields.String(readonly=True, description="Slug of tag"),
})

post_model = api.model("Post", {
    "id": fields.Integer(readonly=True, description="ID of post"),
    "title": fields.String(required=True, description="Title of post"),
    "slug": fields.String(readonly=True, description="Slug of post"),
    "body": fields.String(required=True, description="Body of post"),
    "tags": fields.List(fields.Nested(tag_model), description="Post tags")
})


@api.route("/")
class PostList(Resource):
    """Shows a list of all posts, and lets you POST to add new post"""

    @api.doc("list_posts")
    @api.marshal_list_with(post_model, envelope="data")
    def get(self):
        """List of all posts"""

        return get_all_posts()

    @api.doc("create_post")
    @api.expect(post_model)
    @api.marshal_with(post_model, code=201)
    def post(self):
        """Create a new post"""

        data = request.json
        post = create_post(data=data)
        return post, 201


@api.route("/<int:post_id>")
@api.response(404, "Post not found")
@api.param("post_id", "The post identifier")
class Post(Resource):
    """Show a single post item and lets you delete them"""

    @api.doc("get_post")
    @api.marshal_with(post_model)
    def get(self, post_id):
        """Get a post given its identifier"""

        try:
            return get_post(post_id)
        except NoResultFound:
            return api.abort(404, f"Post {post_id} doesn\'t exist")

    @api.doc("delete_post")
    @api.response(204, "post deleted")
    def delete(self, post_id):
        """Delete a post given its identifier"""

        delete_post(post_id)
        return "", 204

    @api.expect(post_model)
    @api.marshal_with(post_model)
    def put(self, post_id):
        """Update a post given its identifier"""

        try:
            data = request.json
            return change_post(post_id, data)
        except NoResultFound:
            return api.abort(404, f"Post {post_id} doesn\'t exist")


@api_tags.route("/")
class TagList(Resource):
    """Shows a list of all tags, and lets you POST to add new tags"""

    @api_tags.doc("list_tags")
    @api_tags.marshal_list_with(tag_model, envelope="data")
    def get(self):
        """List of all tags"""

        return get_all_tags()

    @api_tags.doc("create_tag")
    @api_tags.expect(tag_model)
    @api_tags.marshal_with(tag_model, code=201)
    def post(self):
        """Create a new tag"""

        data = request.json
        tag = create_tag(data=data)
        return tag, 201


@api_tags.route("/<int:tag_id>")
@api_tags.response(404, "Tag not found")
@api_tags.param("tag_id", "The tag identifier")
class Tag(Resource):
    """Show a single tag item and lets you delete them"""

    @api_tags.doc("get_tag")
    @api_tags.marshal_with(tag_model)
    def get(self, tag_id):
        """Get a tag given its identifier"""

        try:
            return get_tag(tag_id)
        except NoResultFound:
            return api.abort(404, f"Tag {tag_id} doesn\'t exist")

    @api_tags.doc("delete_tag")
    @api_tags.response(204, "tag deleted")
    def delete(self, tag_id):
        """Delete a tag given its identifier"""

        delete_tag(tag_id)
        return "", 204

    @api_tags.expect(tag_model)
    @api_tags.marshal_with(tag_model)
    def put(self, tag_id):
        """Update a tag given its identifier"""

        try:
            data = request.json
            return change_tag(tag_id, data)
        except NoResultFound:
            return api.abort(404, f"Tag {tag_id} doesn\'t exist")
