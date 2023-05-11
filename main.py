from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def Index():
    return render_template("index.html")


@app.route("/name")
def hello():
    return f"hello Name"


@app.route("/name/<path:age>")
def age(age):
    return f"Show your age is {age}"


if __name__ == "__main__":
    app.run(debug=True)
