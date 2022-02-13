from app import db
from app.models.product import Product
from app.models.schemas import ProductSchema

from tests.utils.base import BaseTestCase

class TestProductModel(BaseTestCase):
    def test_create_product(self):
        d = Product(name='test1', price='1', image_url='test1', detailed_info='test detail info', menu_id=1)
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_product(self):
        d = Product(name='test2', price='1', image_url='test1', detailed_info='test detail info', menu_id=1)
        db.session.add(d)
        db.session.commit()
        d.name = 'test4'
        db.session.commit()
        self.assertTrue(d.name == 'test4')

    def test_delete_product(self):
        d = Product(name='test3', menu_id=1)
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Product.query.get(d.id)
        self.assertTrue(res is None)

    def test_schema(self):
        d = Product(name='test5', menu_id=1)
        d_dump = ProductSchema().dump(d)
        self.assertTrue(d_dump['name'] == 'test5')