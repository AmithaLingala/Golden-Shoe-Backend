from flask import request
from flask_restful import Resource, reqparse
from models.product_model import ProductModel,db

class Product(Resource):
    def get(self,name):
        product = ProductModel.query.filter_by(name=name).first()
        if product:
            return product.json()
        return {'message':'product not found'},404
 
    def put(self,name):
        data = request.get_json()
 
        product = ProductModel.query.filter_by(name=name).first()
 
        if product:
            product.price = data["price"]
            product.size = data["size"] 
            product.color = data["color"]
            product.img_url = data["img_url"]
            product.stock = data["stock"]
            product.gender = data["gender"]
            product.style = data["style"]
        else:
            product = ProductModel(name=name,**data)
 
        db.session.add(product)
        db.session.commit()
 
        return product.json()
 
    def delete(self,name):
        product = ProductModel.query.filter_by(name=name).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return {'message':'Deleted'}
        else:
            return {'message': 'product not found'},404