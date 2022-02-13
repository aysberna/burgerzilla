from app import db
from app.models.menu import Menu
from app.models.schemas import MenuSchema

from tests.utils.base import BaseTestCase

class TestMenuModel(BaseTestCase):
    def test_create_menu(self):
        d = Menu(name='test1',restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.id > 0)

    def test_update_menu(self):
        d = Menu(name='test2',restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        d.name = 'test4'
        db.session.commit()
        self.assertTrue(d.name == 'test4')

    def test_delete_menu(self):
        d = Menu(name='test3',restaurant_id=1)
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Menu.query.get(d.id)
        self.assertTrue(res is None)

    def test_schema(self):
        d = Menu(name='test5',restaurant_id=1)
        d_dump = MenuSchema().dump(d)
        self.assertTrue(d_dump['name'] == 'test5')