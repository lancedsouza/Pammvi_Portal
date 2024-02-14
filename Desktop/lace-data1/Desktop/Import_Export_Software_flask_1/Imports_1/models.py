# Set up db inside the __init__.py under myproject folder

from Imports_1 import db



class Supplier(db.Model):
    __tablename__ = 'supplier'

    # Explicitly mark this column as the primary key
    supplier_id = db.Column(db.Integer, primary_key=True,nullable=False)
    supplier_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
        # One to Many relationship

    products = db.relationship('Products', backref='supplier', lazy='dynamic')


    class Products(db.Model):
        __tablename__ = 'products'

        id = db.Column(db.Integer, primary_key=True)
        supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
        product_name = db.Column(db.String(255), nullable=False)
        product_category = db.Column(db.String(50), nullable=False)
        product_vertical = db.Column(db.String(20), nullable=False)
        ean_code = db.Column(db.String(20), nullable=False)
        color = db.Column(db.String(20), nullable=False)
        power = db.Column(db.String(20), nullable=False)
        label = db.Column(db.String(20), nullable=False)
        packing = db.Column(db.String(20), nullable=False)        
        unit_price = db.Column(db.Float, nullable=False)
        country = db.Column(db.String(50), nullable=False)
        currency = db.Column(db.String(50), nullable=False)
        qty = db.Column(db.Integer, nullable=False)

        # One to One relationship
        suppliers= db.relationship('Supplier', backref='products', uselist=False)

        def __repr__(self):
            return f"Product name is {self.product_name} product_id is {self.id} and supplier is {self.supplier.name}, supplier_id is {self.supplier.supplier_id} and quantity is {self.qty}"





class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'

    order_id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    qty = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    net_price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    # One to Many
    suppliers = db.relationship('Supplier', backref='PurchaseOrder', lazy='dynamic')
    products = db.relationship('Products', backref='PurchaseOrder', lazy='dynamic')

    def __repr__(self):
        return f'<PurchaseOrder {self.order_id}>'