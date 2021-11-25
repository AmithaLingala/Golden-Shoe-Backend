from flask import request
from flask_restful import Resource, reqparse
from models.product_model import ProductModel, db

class Products(Resource):
    def get(self):
        products = ProductModel.query.all()
        return {'products':list(x.json() for x in products)}

    def post(self):
        data = request.get_json()
        product = ProductModel(**data)
        db.session.add(product)
        db.session.commit()
        return product.json()