# Data Transfer Objects for customer services
from flask_restx import Namespace,fields

class CustomerDto:
    api = Namespace("customers", description="Customer related operations")
    customer = api.model("customers", {
        'id':fields.Integer,
        'no':fields.String,
        'restaurant_id':fields.Integer,
        'user_id':fields.Integer,
        'menu_id':fields.Integer,
        'status':fields.String
    })

    customer_resp = api.model("Customer Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'customer':fields.Nested(customer)
    })

    customer_list_resp = api.model("Customer List Response", {
        'status':fields.Boolean,
        'message':fields.String,
        'customers':fields.List(fields.Nested(customer))})