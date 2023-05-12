from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/coffees")
def coffees():
    return render_template("coffees.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
