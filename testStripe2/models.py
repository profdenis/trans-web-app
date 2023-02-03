from app import db
import datetime


class DBUser(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.Text(), primary_key=True)
    email = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Text())
    password = db.Column(db.Text(), nullable=False)
    cart_id = db.Column(db.Integer(), db.ForeignKey('cart.cart_id'))

    def __repr__(self):
        return f"<DBUser {self.username}: {self.email}>"


class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer(), nullable=False, default=0)
    carts = db.relationship('Cart', secondary='product_cart', backref=db.backref('carts', lazy=True), lazy=True,
                            viewonly=True)

    def __repr__(self):
        return f"<Product {self.product_id}: {self.name} {self.price}>"


class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
    products = db.relationship('Product', secondary='product_cart', backref=db.backref('products', lazy=True),
                               lazy=True)

    def __repr__(self):
        return f"<Cart {self.cart_id}: {self.datetime}>"


class ProductCart(db.Model):
    __tablename__ = 'product_cart'
    product_id = db.Column(db.Integer(), db.ForeignKey('product.product_id'), primary_key=True)
    cart_id = db.Column(db.Integer(), db.ForeignKey('cart.cart_id'), primary_key=True)
    quantity = db.Column(db.Integer(), default=1)

    def __repr__(self):
        return f"<ProductCart {self.product_id} {self.cart_id}: {self.quantity}>"
