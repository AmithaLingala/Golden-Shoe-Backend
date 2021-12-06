from flask import request
from flask_restful import Resource, reqparse
from models.product_model import ProductModel,db
import json

class Product(Resource):
    def get(self,name):
        curColor= request.args.get('color')
        curSize= request.args.get('size')
        products = ProductModel.query.filter_by(name=name,color=curColor)
        colorsCursor = db.session.query(ProductModel.color).distinct().filter(ProductModel.name==name).all()
        colors = [result[0] for result in colorsCursor]
        if products.count():
            # print(next(filter(lambda product:product.size==int(curSize),products),None))
            product = products[0] if not curSize else next(filter(lambda product: product.size==int(curSize),products),None)
            product = product.json()
            product["sizes"] = [{"size":product.size,"stock":product.stock} for product in products]
            product["colors"] = colors
            return product
        return {'message':'product not found'},404

    def put(self,id):
        data = request.get_json()
 
        product = ProductModel.query.filter_by(id=id).first()
 
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