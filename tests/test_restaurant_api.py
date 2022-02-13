import json

from flask_jwt_extended import create_access_token

from app import db
from app.models.restaurant import Restaurant

from utils.base import BaseTestCase

def get_restaurant_data(self,accesstoken,restaurant_id):
    return self.client.get(
        f"/api/restaurants/{restaurant_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def get_restaurants_data(self,accesstoken):
    return self.client.get(
        f"/api/restaurants",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def post_restaurant_data(self,accesstoken,restaurant_data,user_id):
    return self.client.post(
        f"/api/restaurants/user/{user_id}",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def put_restaurant_data(self,accesstoken,restaurant_data,restaurant_id,user_id):
    return self.client.put(
        f"/api/restaurants/{restaurant_id}/user/{user_id}",
        data=json.dumps(restaurant_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def delete_restaurant_data(self,accesstoken,restaurant_id):
    return self.client.delete(
        f"/api/restaurants/{restaurant_id}",
        headers={"Authorization": "Bearer " + accesstoken},
    )

class TestRestaurantBlueprint(BaseTestCase):
    def test_restaurant_get(self):
        """
        Test for getting a restaurant
        """
        d = Restaurant(name='test1',user_id=1)
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=1)
        restaurant_resp = get_restaurant_data(self,access_token,d.id)
        restaurant_data = json.loads(restaurant_resp.data.decode())

        self.assertTrue(restaurant_resp.status_code == 200)
        self.assertTrue(restaurant_data['restaurant']['name'] == 'test1')
        self.assertTrue(restaurant_data['restaurant']['user_id'] == 1)

        data_404_resp = get_restaurant_data(self,access_token,100)
        self.assertEquals(data_404_resp.status_code, 400)
