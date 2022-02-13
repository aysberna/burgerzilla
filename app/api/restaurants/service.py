# Restaurant Services

from flask import current_app
from app.models.schemas import RestaurantSchema, MenuSchema, ProductSchema, OrderSchema

from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import get_jwt_identity
from app.models.restaurant import Restaurant
from app.models.menu import Menu
from app.models.product import Product
from app.models.order import Order

from app import db

class RestaurantService:
    @staticmethod
    def get_restaurant(restaurant_id: int):
        """
        Get a restaurant by id"""
        if not (restaurant := Restaurant.query.get(restaurant_id)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        from .utils import load_restaurant_data
        try:
            restaurant_data = load_restaurant_data(restaurant)
            resp=message(True,"Restaurants loaded successfully")
            resp["restaurant"]=restaurant_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant(restaurant_id: int):
        """
        Delete a restaurant by id"""
        if not (restaurant := Restaurant.query.get(restaurant_id)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        try:
            db.session.delete(restaurant)
            db.session.commit()
            return message(True,"Restaurant deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_restaurant(user_id: int,restaurant_data):
        """
        Insert a new restaurant"""
        try:
            current_user = get_jwt_identity()
            restaurant = Restaurant(name=restaurant_data["name"],user_id=current_user)
            db.session.add(restaurant)
            db.session.commit()
            return message(True,"Restaurant created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_restaurant(restaurant_id: int,restaurant_data):
        """
        update a restaurant"""
        if not (restaurant:=Restaurant.query.get(restaurant_id)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        try:
            Restaurant.query.filter_by(id=restaurant_id).update(restaurant_data)
            db.session.commit()
            return message(True,"Restaurant updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
    @staticmethod
    def get_restaurants(user_id: int):
        """
        Get all restaurants of a specific user"""
        if not(restaurants := Restaurant.query.filter_by(user_id=user_id)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        from .utils import load_restaurant_data
        try:
            restaurants_data = [load_restaurant_data(restaurant) for restaurant in restaurants]
            resp=message(True,"Restaurants loaded successfully")
            resp["restaurants"]=restaurants_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    
    @staticmethod
    def get_menu():
        """
        get a menu by id"""
        current_user = get_jwt_identity()
        if not (menu := Menu.query.get(current_user)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        from .utils import load_menu_data
        try:
            menu_data = load_menu_data(menu)
            resp=message(True,"Menu loaded successfully")
            resp["menu"]=menu_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_menu(menu_data):
        """
        Insert a new menu"""
        try:
            current_user = get_jwt_identity()
            menu = Menu(name=menu_data["name"],restaurant_id=current_user)
            db.session.add(menu)
            db.session.commit()
            return message(True,"Menu created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_menu(menu_id: int,menu_data):
        """
        update a menu"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(msg="Restaurant not found",reason='',code=400)
        try:
            Menu.query.filter_by(id=menu_id).update(menu_data)
            db.session.commit()
            return message(True,"Menu updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_products(menu_id: int):
        """
        Get all products of a specific menu"""
        if not(products := Product.query.filter_by(menu_id=menu_id)):
            return err_resp(msg="Product not found",reason='',code=400)
        from .utils import load_product_data
        try:
            products_data = [load_product_data(product) for product in products]
            resp=message(True,"Product loaded successfully")
            resp["products"]=products_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_product(product_id: int):
        """
        Get a product by id"""
        if not (product := Product.query.get(product_id)):
            return err_resp(msg="Product not found",reason='',code=400)
        from .utils import load_product_data
        try:
            product_data = load_product_data(product)
            resp=message(True,"Product loaded successfully")
            resp["product"]=product_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_product(product_data, menu_id: int):
        """
        Insert a new product"""
        try:
            product = Product(name=product_data["name"],detailed_info=product_data["detailed_info"],price=product_data["price"],image_url=product_data["image_url"],menu_id=menu_id)
            db.session.add(product)
            db.session.commit()
            return message(True,"Product created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_product(product_id: int,product_data):
        """
        Update a product"""
        if not (product:=Product.query.get(product_id)):
            return err_resp(msg="Product not found",reason='',code=400)
        try:
            Product.query.filter_by(id=product_id).update(product_data)
            db.session.commit()
            return message(True,"Product updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_product(product_id: int):
        """
        Delete a product by id"""
        if not (product := Product.query.get(product_id)):
            return err_resp(msg="Product not found",reason='',code=400)
        try:
            db.session.delete(product)
            db.session.commit()
            return message(True,"Product deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


    @staticmethod
    def get_orders():
        """
        Get all order of a specific restaurant"""
        current_user = get_jwt_identity()

        if not(orders := Order.query.filter_by(user_id=current_user)):
            return err_resp(msg="Order not found",reason='',code=400)
        from .utils import load_order_data
        try:
            orders_data = [load_order_data(order) for order in orders]
            resp=message(True,"Orders loaded successfully")
            resp["orders"]=orders_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_order(order_id: int):
        """
        Delete a order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(msg="Order not found",reason='',code=400)
        try:
            # Deleted with order detail
            db.session.delete(order)
            db.session.commit()
            return message(True,"Order deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_order(order_id: int):
        """
        Get an order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(msg="Order not found",reason='',code=400)
        from .utils import load_order_data, load_order_detail_data
        try:
            order_detail = order.items
            detail = [load_order_detail_data(item) for item in order_detail]
            order_data = load_order_data(order)
            # Added items in order
            order_data['items'] = detail
            resp=message(True,"Orders loaded successfully")
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order(order_id: int,order_data):
        """
        update an order"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",reason='',code=400)
        try:
            Order.query.filter_by(id=order_id).update(order_data)
            db.session.commit()
            return message(True,"Order updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()