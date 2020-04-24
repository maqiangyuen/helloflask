from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    # 获取查询参数name的值
    name = request.args.get("name", "Flask")
    return "<h1>Hello, {}!</h1>".format(name)
