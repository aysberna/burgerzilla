# Routes for user services

from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required


from .service import UserService
from .dto import UserDto

api  = UserDto.api
data_resp = UserDto.data_resp

@api.route("/<string:username>")
class UserGet(Resource):
    @api.doc("get specified user data",responses={
        200:("Success",data_resp),
        404:"User Not Found",
    })
    @jwt_required()
    def get(self,username):
        """get user data"""
        return UserService.get_user_data(username)
    

