# Routes for restaurants services

from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


from .service import RestaurantService
from .dto import RestaurantDto

api = RestaurantDto.api
restaurant=RestaurantDto.restaurant
restaurant_resp=RestaurantDto.restaurant_resp
restaurant_list_resp=RestaurantDto.restaurant_list_resp
menu=RestaurantDto.menu
product=RestaurantDto.product
product_resp=RestaurantDto.product_resp
order=RestaurantDto.order

@api.route('/<int:restaurant_id>')
class Restaurant(Resource):
    @api.doc('Get specific restaurant',responses={200:("Success",restaurant_resp), 400:"Invalid product ID",})
    @jwt_required()
    def get(self,restaurant_id):
        """ get specific restaurant"""
        return RestaurantService.get_restaurant(restaurant_id)
    
    @api.doc("Delete a specific restaurant",responses={200:"Success"})
    @jwt_required()
    def delete(self,restaurant_id):
        """ Delete a specific restaurant"""
        return RestaurantService.delete_restaurant(restaurant_id)

    @api.doc("Update a specific restaurant",responses={200:"Success"})
    @api.expect(restaurant)
    @jwt_required()
    def put(self,restaurant_id):
        """ Update a specific restaurant"""
        data = request.get_json()
        return RestaurantService.update_restaurant(restaurant_id,data)

@api.route("/user/<int:user_id>")
class RestaurantList(Resource):
    @api.doc("Get all restaurant of a specific user",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,user_id):
        """
        Get all restaurant of a specific user"""
        return RestaurantService.get_restaurants(user_id)


    @api.doc("Create a new restaurant",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(restaurant)
    @jwt_required()
    def post(self,user_id):
        """
        Create a new restaurant"""
        data = request.get_json()
        return RestaurantService.insert_restaurant(user_id,data)

@api.route("/menu")
# TODO:Giren kullanıcının id si restaurant id si ise o zaman işlemler yapılsın
class MenuList(Resource):
    @api.doc("Get all menu of a specific restaurant",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self):
        """
        Get all menu of a specific restaurant"""
        return RestaurantService.get_menu()

    @api.doc("Create a new menu",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(restaurant)
    @jwt_required()
    def post(self):
        """
        Create a new restaurant"""
        data = request.get_json()
        return RestaurantService.insert_menu(data)

@api.route('/menu/<int:menu_id>')
class Menu(Resource):
    @api.doc("Update a menu for restaurant",responses={200:"Success"})
    @api.expect(menu)
    @jwt_required()
    def put(self, menu_id):
        """ Update a menu"""
        data = request.get_json()
        return RestaurantService.update_menu(menu_id,data)

@api.route("/menu/<int:menu_id>/product")
class ProductList(Resource):
    @api.doc("Get all products of a specific menu",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self, menu_id):
        """
        Get all products of a specific menu"""
        return RestaurantService.get_products(menu_id)

    @api.doc("Create a new product",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(product)
    @jwt_required()
    def post(self, menu_id):
        """
        Create a new product"""
        data = request.get_json()
        return RestaurantService.insert_product(data,menu_id)


@api.route('/product/<int:product_id>')
class Product(Resource):
    @api.doc('Get specific product',products={
        200:("Success",product_resp),
        400:"Invalid product ID",
    })
    @jwt_required()
    def get(self,product_id):
        """ Get specific product"""
        return RestaurantService.get_product(product_id)

    @api.doc("Update a specific product",responses={200:"Success"})
    @api.expect(product)
    @jwt_required()
    def put(self,product_id):
        """ Update a specific restaurant"""
        data = request.get_json()
        return RestaurantService.update_product(product_id,data)

    @api.doc("Delete a specific product",responses={200:"Success"})
    @jwt_required()
    def delete(self,product_id):
        """ Delete a specific product"""
        return RestaurantService.delete_product(product_id)


@api.route('/order')
class Order(Resource):
    @api.doc("Get all order of a specific customer",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self):
        """
        Get all order of a specific customer"""
        return RestaurantService.get_orders()


@api.route("/order/<int:order_id>")
# TODO:Giren kullanıcının id si restaurant id si ise o zaman işlemler yapılsın
class OrderList(Resource):
    @api.doc("Get an order for a specific user",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,order_id):
        """
        Get an order"""
        return RestaurantService.get_order(order_id)

    @api.doc("Delete a specific order",responses={200:"Success"})
    @jwt_required()
    def delete(self,order_id):
        """ Delete a specific order"""
        return RestaurantService.delete_order(order_id)
    
    @api.doc("Update a specific order",responses={200:"Success"})
    @api.expect(order)
    @jwt_required()
    def put(self,order_id):
        """ Update a specific order"""
        data = request.get_json()
        return RestaurantService.update_order(order_id,data)