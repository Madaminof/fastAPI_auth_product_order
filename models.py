from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # 'user' -> 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'  # 'product' -> 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    orders = relationship('Order', back_populates='product')

class Order(Base):
    __tablename__ = 'orders'  # 'order' -> 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')
