from app import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    detailed_info = db.Column(db.String(256))
    price = db.Column(db.String(32))
    image_url = db.Column(db.String(256))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

    def __repr__(self):
        return '<Product {}>'.format(self.name)

    @staticmethod
    def insert_product():
        default_product = Product(name='Bombili burger', 
        detailed_info='Meşhur dombili burger, özel soslu, sarmısaklı ve soğanlı', 
        price='30', image_url='https://picjumbo.com/yummy-pulled-pork-burger/', menu_id='1')
        db.session.add(default_product)
        db.session.commit()
        default_product2 = Product(name='Duble Peynirli', 
        detailed_info='Çift katlı, mozerella ve çedarla bezenmiş dombili burger', 
        price='50', image_url='https://picjumbo.com/yummy-pulled-pork-burger/', menu_id='1')
        db.session.add(default_product2)
        db.session.commit()
        default_product3 = Product(name='Tek Katlı', 
        detailed_info='Bol domatesli, özel muble soslu', 
        price='25', image_url='https://picjumbo.com/yummy-pulled-pork-burger/', menu_id='2')
        db.session.add(default_product3)
        db.session.commit()