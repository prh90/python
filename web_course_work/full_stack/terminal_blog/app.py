from menu import Menu
from models.post import Post
from database import Database
from models.blog import Blog

Database.initialize()

menu = Menu()
menu.run_menu()
# post = Post(blog_id="123",
#             title="Post",
#             content="THIS IS SOME SAMPLE STUFF",
#             author="Pablo")
# post.save_to_mongo()

# post = Post.from_mongo('2614e402162d45c585ca8b9baa5b4a7a')
#
# print(post)
# blog = Blog(author="Pablo",
#             title="Sample Title",
#             description="Sample Description")
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.get_from_mongo(blog.id)
#
# print(blog.get_posts())
