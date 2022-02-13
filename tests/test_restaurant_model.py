from app import db
from app.models.restaurant import Restaurant
from app.models.schemas import RestaurantSchema

from tests.utils.base import BaseTestCase

class TestRestaurantModel(BaseTestCase):
    def test_create_restaurant(self):
        d = Restaurant(name='test1',user_id=1)
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_restaurant(self):
        d = Restaurant(name='test2',user_id=1)
        db.session.add(d)
        db.session.commit()
        d.name = 'test4'
        db.session.commit()
        self.assertTrue(d.name == 'test4')

    def test_delete_restaurant(self):
        d = Restaurant(name='test3',user_id=1)
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Restaurant.query.get(d.id)
        self.assertTrue(res is None)

    def test_schema(self):
        # d = Restaurant(user_id=1)
        d = Restaurant(name='test5',user_id=1)
        d_dump = RestaurantSchema().dump(d)
        self.assertTrue(d_dump['name'] == 'test5')
    
