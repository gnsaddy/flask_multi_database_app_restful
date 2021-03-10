from flask import Flask, request, jsonify, make_response
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from database.models import *
from database.db import initialize_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:system12345@localhost:3306/product'

app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///user.db',
    'items': 'sqlite:///item.db'
}
initialize_db(app)


class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
        print("in", db)

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)


@app.route('/products', methods=['GET'])
def index():
    get_products = Product.query.all()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))


@app.route('/products/<id>', methods=['GET'])
def get_product_by_id(id):
    get_product = Product.query.get(id)
    product_schema = ProductSchema()
    product = product_schema.dump(get_product)
    return make_response(jsonify({"product": product}))


@app.route('/products/<id>', methods=['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    get_product = Product.query.get(id)
    if data.get('title'):
        get_product.title = data['title']
    if data.get('productDescription'):
        get_product.productDescription = data['productDescription']
    if data.get('productBrand'):
        get_product.productBrand = data['productBrand']
    if data.get('price'):
        get_product.price = data['price']
    db.session.add(get_product)
    db.session.commit()
    product_schema = ProductSchema(only=['id', 'title', 'productDescription', 'productBrand', 'price'])
    product = product_schema.dump(get_product)
    return make_response(jsonify({"product": product}))


@app.route('/products/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    get_product = Product.query.get(id)
    db.session.delete(get_product)
    db.session.commit()
    return make_response("", 204)


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema()
    product = product_schema.load(data)
    result = product_schema.dump(product.create())
    return make_response(jsonify({"product": result}), 200)


# user schema
class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Users
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)


@app.route('/user', methods=['GET'])
def user():
    get_user = Users.query.all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_user)
    return make_response(jsonify({"user": users}))


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)
    result = user_schema.dump(user.create())
    return make_response(jsonify({"user": result}), 200)


# item schema
class ItemSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Items
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    itemDescription = fields.String(required=True)
    itemBrand = fields.String(required=True)
    price = fields.Number(required=True)


@app.route('/item', methods=['GET'])
def Item():
    get_item = Items.query.all()
    item_schema = ItemSchema(many=True)
    item = item_schema.dump(get_item)
    return make_response(jsonify({"item": item}))


@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    user_schema = UserSchema()
    item = user_schema.load(data)
    result = user_schema.dump(item.create())
    return make_response(jsonify({"item": result}), 200)


if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)
