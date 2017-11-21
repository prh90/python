from models.post import Post
from database import Database

Database.initialize()

# post = Post(blog_id="123",
#             title="Post",
#             content="THIS IS SOME SAMPLE STUFF",
#             author="Pablo")
# post.save_to_mongo()

# post = Post.from_mongo('2614e402162d45c585ca8b9baa5b4a7a')
#
# print(post)
