from app import db

class Menu(db.Model):
    __tablename__ = 'menu'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def __repr__(self):
        return '<Menu {}>'.format(self.name)

    @staticmethod
    def insert_menu():
        default_menu = Menu(name='Dombili burger menu', restaurant_id='1')
        db.session.add(default_menu)
        db.session.commit()
        default_menu2 = Menu(name='Dublemumble burger menu', restaurant_id='2')
        db.session.add(default_menu2)
        db.session.commit()