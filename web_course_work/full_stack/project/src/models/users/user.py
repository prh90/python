import uuid
from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that email/password combo is valid or not
        Check if the email exists and that the password associated to that email is correct
        """
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            raise UserErrors.UserNotExistsError("Your user does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your password is incorrect")
