from app import db

class OrderDetail(db.Model):
    __tablename__ = 'order_detail'
    
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

    def __repr__(self):
        return '<Order Detail {}>'.format(self.order_id)

    def to_json(self):
        return {
            'product': self.product_id,
            'quantity': self.quantity
        }  