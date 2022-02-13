import enum
from app import db

class OrderStatus(enum.Enum):
    YENI = "Yeni"
    HAZIRLANIYOR = "Hazırlanıyor"
    YOLDA = "Yolda"
    TESLIM = "Teslim"
    IPTAL = "Müşteri iptal"
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.String(64), unique=True)
    status = db.Column(db.Enum(OrderStatus))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    items = db.relationship('OrderDetail', backref='orderDetail')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def __repr__(self):
        return '<Order {}>'.format(self.no)

    def to_json(self):
        items = []
        for i in self.items:
            items.append(i.to_json())

        return {
            'items': items,
            'no': self.no,
            'status': self.status,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id
        }