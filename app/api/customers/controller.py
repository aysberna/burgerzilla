# Routes for customer services

from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import CustomerService
from .dto import CustomerDto

api = CustomerDto.api
order=CustomerDto.customer
order_resp=CustomerDto.customer_resp
order_list_resp=CustomerDto.customer_list_resp

@api.route('/order')
class Order(Resource):
    @api.doc("Get all order of a specific customer",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self):
        """
        Get all order of a specific customer"""
        return CustomerService.get_orders()

@api.route("/order/restaurant/<int:restaurant_id>")
class OrderRestaurantList(Resource):

    @api.doc("Create a new order",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(order)
    @jwt_required()
    def post(self,restaurant_id):
        """
        Create a new restaurant"""
        data = request.get_json()
        return CustomerService.insert_order(restaurant_id,data)

@api.route("/order/<int:order_id>")
class OrderList(Resource):
    @api.doc("Get an order for a specific user",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,order_id):
        """
        Get an order"""
        return CustomerService.get_order(order_id)

    @api.doc("Delete a specific order",responses={200:"Success"})
    @jwt_required()
    def delete(self,order_id):
        """ Delete a specific order"""
        return CustomerService.delete_order(order_id)
    
    @api.doc("Update a specific order",responses={200:"Success"})
    @api.expect(order)
    @jwt_required()
    def put(self,order_id):
        """ Update a specific order"""
        data = request.get_json()
        return CustomerService.update_order(order_id,data)