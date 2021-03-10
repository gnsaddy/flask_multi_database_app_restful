from database.db import db


class Users(db.Model):
    __bind_key__ = 'users'
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, productDescription, productBrand, price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price

    def __repr__(self):
        return str(self.id)


class Items(db.Model):
    __bind_key__ = 'items'
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    itemDescription = db.Column(db.String(100))
    itemBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, itemDescription, itemBrand, price):
        self.title = title
        self.itemDescription = itemDescription
        self.itemBrand = itemBrand
        self.price = price

    def __repr__(self):
        return str(self.id)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, productDescription, productBrand, price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price

    def __repr__(self):
        return str(self.id)



