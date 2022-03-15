import sqlalchemy as sql

import database

class Products(database.Base):
    __tablename__ = 'products'
    index = sql.Column(sql.Integer, primary_key=True)
    id_product = sql.Column(sql.Integer)
    name = sql.Column(sql.Text)
    category = sql.Column(sql.Text)
    price = sql.Column(sql.Numeric)

class Orders(database.Base):
    __tablename__ = 'orders'
    index = sql.Column(sql.Integer, primary_key=True)
    id_order = sql.Column(sql.Integer)
    month = sql.Column(sql.Text)
    city = sql.Column(sql.Text)
    state = sql.Column(sql.Text)
    region = sql.Column(sql.Text)
    time_separate = sql.Column(sql.Float)
    
class OrdersProducts(database.Base):
    __tablename__ = 'orders_products'
    index = sql.Column(sql.Integer, primary_key=True)
    id_order = sql.Column(sql.Integer)
    id_product = sql.Column(sql.Integer)
    quantity = sql.Column(sql.Integer)
