from flask import Flask,request
from flask_restful import Api, Resource, reqparse
from apis.product import Product
from apis.products import Products
from models.product_model import db
app = Flask(__name__)
 
api = Api(app) #Flask REST Api code 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golden_shoe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Products, '/products')
api.add_resource(Product,'/product/<string:name>')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)