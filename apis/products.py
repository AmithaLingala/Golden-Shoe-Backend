from flask import request
from flask_restful import Resource, reqparse
from models.product_model import ProductModel, db

class Products(Resource):
    def get(self):
        products = ProductModel.query.all()
        return {'products':list(x.json() for x in products)}
 