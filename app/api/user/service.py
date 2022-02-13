# User Services

from flask import current_app

from app.utils import err_resp,internal_err_resp, message
from app.models.user import User

class UserService:
    @staticmethod
    def get_user_data(username):
        """
        get user data"""
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found","user_404",404)
        
        from .utils import load_data

        try:
            user_data = load_data(user)
            resp = message(True,"User data sent")
            resp["user"] = user_data
            return resp,200
        except Exception as e:
            print("Error User:",e)
            current_app.logger.error(e)
            return internal_err_resp()
            