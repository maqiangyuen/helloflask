
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/block", defaults={"name": "dad"})
# @app.route("/block/<name>")
# def whos_you_dad(name):
#     return "<h1>Hello, {}!</h1>".format(name)



# ------------------ or ------------------------
from flask import Flask

app = Flask(__name__)

@app.route("/hi")
@app.route("/hi/<name>")
def red(name="joj"):
    return "<h1>Hello, {}!</h1>".format(name)