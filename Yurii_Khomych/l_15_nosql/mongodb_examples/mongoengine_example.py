from mongoengine import *

connect("mydb", "default", host="localhost")
from mongoengine_models import Post, Author


# post_1 = Post(
#     title="Sample Post", content="Some engaging content", author="Scott"
# )
# post_1.save()  # This will perform an insert
# print(post_1.title)
# post_1.title = "A Better Post Title"
# post_1.save()  # This will perform an atomic edit on "title"
# print(post_1.title)
# post_2 = Post(content="Content goes here", author="Michael")
# post_2.save()
# Post.objects

author_1 = Author(name="Jony")
author_1.save()
post_1 = Post(title="Sample Post", content="Content goes here", author=author_1.id)
post_1.save()
Post.objects.first().author.name
