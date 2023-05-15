import os
from flask_wtf.csrf import CSRFProtect
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from Forms import LoginForm

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("login.html", form=login_form)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/coffees")
def coffees():
    return render_template("coffees.html")



@app.route("/shop")
def shop():
    return "<h1>shop</h1>"



@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
