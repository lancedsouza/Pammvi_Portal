import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager=LoginManager()


app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY']='hello'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app, db)
Migrate(app, db,render_as_batch=True)

login_manager.init_app(app)
login_manager.login_view='login'




from my_project.purchase_order.views import purchase_order_blueprint
from my_project.purchase_order.views import success_blueprint
from my_project.purchase_order.views import calculate_net_price_blueprint
from my_project.purchase_order.views import purchase_order_form_blueprint
from my_project.purchase_order.views import enter_num_blueprint
from my_project.purchase_order.views import view_po_blueprint
from my_project.purchase_order.views import enter_po_num_blueprint
from my_project.products.views import enter_products_form_blueprint
from my_project.products.views import enter_num_products_blueprint
from my_project.products.views import view_products_blueprint
from my_project.products.views import view_products_name_blueprint
from my_project.products.views import products_form_blueprint
from my_project.products.views import enter_product_name_blueprint
from my_project.products.views import update_product_name_blueprint
from my_project.products.views import update_product_blueprint
from my_project.products.views import enter_product_id_blueprint





app.register_blueprint(purchase_order_blueprint,url_prefix='/purchase_order')
app.register_blueprint(success_blueprint, url_prefix='/success')
app.register_blueprint(calculate_net_price_blueprint,url_prefix='/calculate_net_price')
app.register_blueprint(purchase_order_form_blueprint,url_prefix='/purchase_order_form')
app.register_blueprint(enter_num_blueprint,url_prefix='/enter_num')
app.register_blueprint(view_po_blueprint,url_prefix='/view_po')
app.register_blueprint(enter_po_num_blueprint,url_prefix='/enter_po_num')
app.register_blueprint(enter_products_form_blueprint,url_prefix='/enter_products_form')
app.register_blueprint(enter_num_products_blueprint,url_prefix='/enter_num_products')
app.register_blueprint(view_products_blueprint,url_prefix='/view_products')
app.register_blueprint(view_products_name_blueprint,url_prefix='/view_products_name')
app.register_blueprint(products_form_blueprint,url_prefix='/products_form')
app.register_blueprint(enter_product_name_blueprint,url_prefix='/enter_product_name')
app.register_blueprint(update_product_name_blueprint,url_prefix='/update_product_name')
app.register_blueprint(update_product_blueprint,url_prefix='/update_product_name')
app.register_blueprint(enter_product_id_blueprint,url_prefix='/enter_product_id')