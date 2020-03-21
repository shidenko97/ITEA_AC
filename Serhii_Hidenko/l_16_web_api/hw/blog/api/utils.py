from blog import db
from blog.posts.models import Post, Tag


def save_changes(data: object):
    """
    Add data to db session and commit it
    :param data: Oblect to save
    :type data: object
    """

    db.session.add(data)
    db.session.commit()


def get_all_posts() -> list:
    """
    Get all posts
    :return: List of posts
    :rtype: list
    """

    return Post.query.order_by(Post.created.desc()).all()


def create_post(data: dict) -> Post:
    """
    Create a post and return it
    :param data: Post parameters
    :type data: dict
    :return: Created post
    :rtype: Post
    """

    tags = []
    if "tags" in data:
        tags = data["tags"]
        del data["tags"]
    post = Post(**data)

    # If list of tags present - add it to post
    for tag in tags:
        post.tags.append(Tag(**tag))
    save_changes(data=post)
    return post


def get_post(post_id: int) -> Post:
    """
    Get post by id
    :param post_id: ID of post
    :type post_id: int
    :return: Post by id
    :rtype: Post
    """

    return Post.query.filter(Post.id == post_id).one()


def delete_post(post_id: int):
    """
    Delete post by id
    :param post_id: ID of post
    :type post_id: int
    """

    Post.query.filter(Post.id == post_id).delete()
    db.session.commit()


def change_post(post_id: int, data: dict) -> Post:
    """
    Change post by id
    :param post_id: ID of post
    :type post_id: int
    :param data: Post parameters
    :type data: dict
    :return: Changed post
    :rtype: Post
    """

    post = get_post(post_id)
    post.title = data["title"]
    post.body = data["body"]
    if "tags" in data:
        for tag in data["tags"]:
            post.tags.append(Tag(**tag))
    save_changes(data=post)
    return post


def get_all_tags() -> list:
    """
    Get all tags
    :return: List of tags
    :rtype: list
    """

    return Tag.query.all()


def create_tag(data: dict) -> Tag:
    """
    Create a tag and return it
    :param data: Tag parameters
    :type data: dict
    :return: Created tag
    :rtype: Tag
    """

    tag = Tag(**data)
    save_changes(data=tag)
    return tag


def get_tag(tag_id: int) -> Tag:
    """
    Get tag by id
    :param tag_id: ID of tag
    :type tag_id: int
    :return: Tag by id
    :rtype: Tag
    """

    return Tag.query.filter(Tag.id == tag_id).one()


def delete_tag(tag_id: int):
    """
    Delete tag by id
    :param tag_id: ID of tag
    :type tag_id: int
    """

    Tag.query.filter(Tag.id == tag_id).delete()
    db.session.commit()


def change_tag(tag_id: int, data: dict) -> Tag:
    """
    Change tag by id
    :param tag_id: ID of tag
    :type tag_id: int
    :param data: Tag parameters
    :type data: dict
    :return: Changed tag
    :rtype: Tag
    """

    tag = get_tag(tag_id)
    tag.name = data["name"]
    save_changes(data=tag)
    return tag
