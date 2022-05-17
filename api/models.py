import sqlalchemy as sql

import database

# sources

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
    id_order = sql.Column(sql.Text)
    date = sql.Column(sql.DateTime)
    location_code = sql.Column(sql.Integer)
    time_separate = sql.Column(sql.Float)
    
class OrdersDetails(database.Base):
    __tablename__ = 'orders_datails'
    index = sql.Column(sql.Integer, primary_key=True)
    id_order = sql.Column(sql.Text)
    id_product = sql.Column(sql.Integer)
    quantity = sql.Column(sql.Integer)

# DW views

class DatesDim(database.Base):
    __tablename__ = 'dates_dim'
    index = sql.Column(sql.Integer, primary_key=True)
    date = sql.Column(sql.DateTime)
    year = sql.Column(sql.Integer)
    quarter = sql.Column(sql.Integer)
    month = sql.Column(sql.Integer)
    day = sql.Column(sql.Integer)
    day_of_week = sql.Column(sql.Integer)
    hour = sql.Column(sql.Integer)

class LocationsDim(database.Base):
    __tablename__ = 'locations_dim'
    index = sql.Column(sql.Integer, primary_key=True)
    location_code = sql.Column(sql.Integer)
    state = sql.Column(sql.Text)
    city = sql.Column(sql.Text)
    region = sql.Column(sql.Text)
    population = sql.Column(sql.Integer)
    size = sql.Column(sql.Text)
    capital = sql.Column(sql.Text)
    
class ProductsDim(database.Base):
    __tablename__ = 'products_dim'
    index = sql.Column(sql.Integer, primary_key=True)
    id_product = sql.Column(sql.Integer)
    name = sql.Column(sql.Text)
    category = sql.Column(sql.Text)

class OrdersFact(database.Base):
    __tablename__ = 'orders_fact'
    index = sql.Column(sql.Integer, primary_key=True)
    id_order = sql.Column(sql.Text)
    date = sql.Column(sql.DateTime)
    location_code = sql.Column(sql.Integer)
    id_product = sql.Column(sql.Integer)
    quantity = sql.Column(sql.Integer)
    unit_price = sql.Column(sql.Numeric)
    prod_final_price = sql.Column(sql.Numeric)