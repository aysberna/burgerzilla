# Data Transfer Objects for authorization services

from flask_restx import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='Authentication related operations')

    user_obj = api.model('User Object', {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role_id": fields.Integer
    })

    auth_login = api.model('Login Data', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    auth_register = api.model('Register Data', 
    { "email": fields.String(required=True, description="User email address"),
        "username": fields.String(required=True, description="User username"),
        "name": fields.String(required=True, description="User name"),
        "password": fields.String(required=True, description="User password")
    })
                
    auth_success = api.model('Auth Success Response', 
    {"status": fields.Boolean,
     "message": fields.String,
     "access_token": fields.String,
     "user": fields.Nested(user_obj)
    })