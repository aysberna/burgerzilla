# Helper methods for restaurant services

from app.models.product import Product
from app.models.schemas import ProductSchema


def load_restaurant_data(restaurant_db_obj):
    from app.models.schemas import RestaurantSchema
    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(restaurant_db_obj)
    return data

def load_menu_data(menu_db_obj):
    from app.models.schemas import MenuSchema
    menu_schema = MenuSchema()
    data = menu_schema.dump(menu_db_obj)
    return data

def load_product_data(product_db_obj):
    from app.models.schemas import ProductSchema
    product_schema = ProductSchema()
    data = product_schema.dump(product_db_obj)
    return data

def load_order_data(order_db_obj):
    from app.models.schemas import OrderSchema
    order_schema = OrderSchema()
    data = order_schema.dump(order_db_obj)
    return data

def load_order_detail_data(order_detail_db_obj):
    from app.models.schemas import OrderDetailSchema
    order_detail_schema = OrderDetailSchema()
    data = order_detail_schema.dump(order_detail_db_obj)
    return data