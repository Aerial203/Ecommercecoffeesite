import os
from threading import currentThread
from unicodedata import category
from flask_wtf.csrf import CSRFProtect
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_bootstrap import Bootstrap
from Forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, current_user, logout_user, UserMixin
from data import data
# from sqlalchemy.sql import text

app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy()
db_name = "dbsqlite.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
USER_ADD_CART = []


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100)) 


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    print(current_user.is_authenticated)
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif user.password != password:
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('shop', category='organic')) 
    return render_template("login.html", form=login_form, current_user=current_user)


@app.route("/register", methods=["POST", "GET"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            print(User.query.filter_by(email=register_form.email.data).first())
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        new_user = User(
            email=register_form.email.data,
            password=register_form.password.data,
            name=register_form.name.data
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('shop', category='organic'))
        
    return render_template("register.html", form=register_form, current_user=current_user)



@app.route("/checkout")
def checkout():
    total = 0
    for t in USER_ADD_CART:
        total += round(float(t['price']), 2)
    return render_template("checkout.html", cart_items = USER_ADD_CART, total=total)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/coffees")
def coffees():
    return render_template("coffees.html")


@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    id = int(request.form.get('product_id'))
    name = request.form.get('product_name')
    price = request.form.get('product_price')

    for cart in USER_ADD_CART:
        if cart != None and cart["id"] == id:
            cart['quantity'] += 1
            break
    else:
        USER_ADD_CART.append({
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        })
        
    return redirect(url_for('shop', category='organic'))



@app.route("/shop/<category>")
def shop(category):
    organic_data, inorganic_data, manufactored_data = data[0]["organic"], data[1]["inorganic"], data[2]["manufactored"]
    
    if category == "organic":
        return render_template('shop.html', data=organic_data)
    elif category == "inorganic":
        return render_template('shop.html', data=inorganic_data)
    else:
        return render_template('shop.html', data=manufactored_data)

@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
