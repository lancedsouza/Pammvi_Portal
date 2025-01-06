from sqlalchemy import Column, Integer, ForeignKey, String, Float, Date
from sqlalchemy.orm import relationship

from my_project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))


    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        

class Supplier(db.Model):
    __tablename__ = 'supplier'
    supplier_id = db.Column(db.Integer, primary_key=True, nullable=False)
    serial_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date) 
    supplier_name = db.Column(db.String(50), nullable=False)
    supplier_address = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(50), nullable=True)
    currency = db.Column(db.String(50), nullable=True)
    qty = db.Column(db.Integer, nullable=False)

    # Establish relationship with Products
    products = db.relationship('Products', backref='supplier', lazy=True)

class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) 
    serial_number = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'), nullable=False)  # Foreign key to Supplier
    product_category = db.Column(db.String(50), nullable=True)
    product_vertical = db.Column(db.String(20), nullable=True)
    ean_code = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    power = db.Column(db.String(20), nullable=False)
    label = db.Column(db.String(20), nullable=False)
    packing = db.Column(db.String(20), nullable=False)        
    unit_price = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(50), nullable=True)
    currency = db.Column(db.String(50), nullable=True)
    qty = db.Column(db.Integer, nullable=False)

    # One to Many relationship with PurchaseOrder
    purchase_order = db.relationship('PurchaseOrder', backref='product', foreign_keys='PurchaseOrder.product_id')

    def __repr__(self):
        return f"Product name is {self.product_name}, product_id is {self.id}, supplier_id is {self.supplier_id}, and quantity is {self.qty}"

class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    reference_num = db.Column(db.String(50), nullable=False, primary_key=True)
    order_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)  # Added date column
    serial_number = db.Column(db.Integer, nullable=False)
    ean_code = db.Column(db.String(50), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))  # Foreign key to Products
    qty = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)        
    product_name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    power = db.Column(db.String(20), nullable=False)
    label = db.Column(db.String(20), nullable=False)
    packing = db.Column(db.String(20), nullable=False)
    supplier_name = db.Column(db.String(50), nullable=False)
    supplier_address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<PurchaseOrder {self.order_id}>'
