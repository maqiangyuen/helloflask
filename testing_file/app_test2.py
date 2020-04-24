from flask import Flask

app = Flask(__name__)

@app.route("/greet/<name>")
def say_hello():
    return "<h1>Hello world, hi {}</h1>".fromat(name)