import json

from flask_jwt_extended import create_access_token

from app import db
from app.models.menu import Menu

from utils.base import BaseTestCase

def get_menu_data(self,accesstoken):
    return self.client.get(
        f"/api/restaurants/menu",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def post_menu_data(self,accesstoken,restaurant_data):
    return self.client.post(
        f"/api/restaurants/menu",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def put_menu_data(self,accesstoken,restaurant_data,menu_id):
    return self.client.put(
        f"/api/restaurants/menu/{menu_id}",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def delete_menu_data(self,accesstoken,menu_id):
    return self.client.delete(
        f"/api/restaurants/menu/{menu_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

class TestMenuBlueprint(BaseTestCase):
    def test_menu_get(self):
        """
        Test for getting a menu
        """
        d = Menu(name='test1',restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=1)
        menu_resp = get_menu_data(self,access_token)

        menu_data = json.loads(menu_resp.data.decode())

        self.assertTrue(menu_resp.status_code == 200)
        self.assertTrue(menu_data['menu']['name'] == 'test1')
