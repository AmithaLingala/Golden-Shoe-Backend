from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class ProductModel(db.Model):
    __tablename__ = 'products'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer())
    size = db.Column(db.Integer())
    color = db.Column(db.String(10))
    img_url = db.Column(db.String(80))
    stock = db.Column(db.Integer())
    gender = db.Column(db.String(10))
    style = db.Column(db.String(20))
 
    def __init__(self, name, price, size, color, img_url, stock, gender, style):
        self.name = name
        self.price = price
        self.size = size 
        self.color = color
        self.img_url = img_url
        self.stock = stock
        self.gender = gender
        self.style = style
     
    def json(self):
        return {
         "name": self.name,
         "price": self.price, 
         "size": self.size, 
         "color": self.color,
         "img_url": self.img_url,
         "stock": self.stock,
         "gender": self.gender,
         "style": self.style
         }