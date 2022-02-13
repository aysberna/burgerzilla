# Data Transfer Objects for restaurant services
from flask_restx import Namespace,fields

class RestaurantDto:
    api = Namespace("restaurants", description="Restaurant related operations")
    restaurant = api.model("restaurants", {
        'id':fields.Integer,
        'name':fields.String,
        'user_id':fields.Integer,
    })

    restaurant_resp = api.model("Restaurant Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurant':fields.Nested(restaurant)
    })

    restaurant_list_resp = api.model("Restaurant List Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurants':fields.List(fields.Nested(restaurant))})

    menu = api.model("menu", {
        'id':fields.Integer,
        'name':fields.String,
        'restaurant_id':fields.Integer,
    })

    product = api.model("products", {
        'id':fields.Integer,
        'name':fields.String,
        'detailed_info':fields.String,
        'price':fields.String,
        'image_url':fields.String,
        'menu_if':fields.Integer
    })
    product_resp = api.model("Product Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'product':fields.Nested(product)
    })

    order = api.model("orders", {
        'id':fields.Integer,
        'no':fields.String,
        'status':fields.String,
        'items':fields.String
    })

    order_resp = api.model("Order Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'orders':fields.List(fields.Nested(order))})