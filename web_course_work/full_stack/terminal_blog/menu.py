from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user_blog = None
        # Ask user for author name
        self.user = input("Enter your author name: ")
        # Check if they've already got an account
        if self._user_has_account:
            print("Welcome back {}".format(self.user))
        # If not, prompt user to create one
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to (R) or (W) blogs?")
        # User read or write blogs
        if read_or_write == 'R':
            pass
        # if read:
            # List blogs in database
            # allow user to pick one
            # display posts
        elif read_or_write == 'W':
            pass
        # if write:
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create a new blog
        else:
            print("Thank you for blogging!")

