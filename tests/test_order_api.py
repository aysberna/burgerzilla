import json

from flask_jwt_extended import create_access_token

from app import db
from app.models.order import Order

from utils.base import BaseTestCase

def get_order_data(self,accesstoken,restaurant_id=1):
    return self.client.get(
        f"/api/restaurants/order/{restaurant_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def post_order_data(self,accesstoken,restaurant_data):
    return self.client.post(
        f"/api/restaurants/order",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def put_menu_data(self,accesstoken,restaurant_data,menu_id):
    return self.client.put(
        f"/api/restaurants/order/{menu_id}",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def delete_menu_data(self,accesstoken,menu_id):
    return self.client.delete(
        f"/api/restaurants/order/{menu_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

class TestMenuBlueprint(BaseTestCase):
    def test_order_get(self):
        """
        Test for getting a order
        """
        d = Order(no='test1',restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=1)
        order_resp = get_order_data(self,access_token,restaurant_id=1)

        order_data = json.loads(order_resp.data.decode())

        self.assertTrue(order_resp.status_code == 200)
        self.assertTrue(order_data['order']['no'] == 'test1')
