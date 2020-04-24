from flask import Flask

app = Flask(__name__)

@app.route("/hi", methods=["GET", "POST"])
def hi():
    return "<h1>Hello world!</h1>"