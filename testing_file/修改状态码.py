# 默认状态码200, 但指定了不同的状态码

from flask import Flask

app = Flask(__name__)

@app.route("/aaa")
def hi():
    return "<h1>Hello world!</h1>", 201

# 有时会想附加或修改某个首部字段。
# 比如，要生成状态码为3XX的重定向响应，
# 需要将首部中的Location字段设置为重定向的目标URL

@app.route("/")
def hello():
    return " ", 302, {"location", "http://www.baidu.com"}

