import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY']='hello'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app, db)




from my_project.purchase_order.views import purchase_order_blueprint
from my_project.purchase_order.views import success_blueprint

app.register_blueprint(purchase_order_blueprint,url_prefix='/purchase_order')
app.register_blueprint(success_blueprint, url_prefix='/success')
