from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #Relationship
    reviews = db.Relationship('Review', back_populates='Review')

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    #Relationship
    reviews = db.Relationship('Review', back_populates='Review')
    
    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    customer_id = db.Column(db.String, db.ForeignKey('customers.id'))
    item_id = db.Column(db.String, db.ForeignKey('items.id'))

    #relationships
    customer = db.Relationship('Customer', back_populates='Review')
    item = db.Relationship('Item', back_populates = 'Review')