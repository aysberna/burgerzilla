from itertools import product
from app import db
from app.models.order import Order
from app.models.schemas import OrderSchema

from tests.utils.base import BaseTestCase

class TestOrderModel(BaseTestCase):
    def test_create_order(self):
        d = Order(no='test1', status='YOLDA', items=[], user_id=1, restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_order(self):
        d = Order(no='test1', status='IPTAL', items=[], user_id=1, restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        d.no = 'test1'
        db.session.commit()
        self.assertTrue(d.no == 'test1')

    def test_delete_order(self):
        d = Order(no='test1', id=1)
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Order.query.get(d.id)
        self.assertTrue(res is None)

    def test_schema(self):
        d = Order(no='test5', status='IPTAL', items=[], user_id=1, restaurant_id=1)
        d_dump = OrderSchema().dump(d)
        self.assertTrue(d_dump['no'] == 'test5')