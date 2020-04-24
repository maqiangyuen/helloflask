from flask import Flask

app = Flask(__name__)

@app.route("/greet/<name>")
def say_hello(name):
    return "<h1>Hello world, hi %s</h1>" % name