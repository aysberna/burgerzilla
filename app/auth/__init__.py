from flask_restx import Api
from flask import Blueprint

from app.models.restaurant import Restaurant
from app.models.order import Order
from app.models.menu import Menu
from app.models.product import Product

from .controller import api as auth_ns

auth_bp = Blueprint('auth', __name__)

auth = Api(auth_bp, title='Authentication', version='1.0')

auth.add_namespace(auth_ns)