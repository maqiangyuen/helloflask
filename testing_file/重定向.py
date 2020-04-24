# from flask import Flask, redirect
#
# app = Flask(__name__)
# @ app.route("/")
# def hi():
#     return redirect("http://www.baidu.com")

# 在程序内重定向到其他视图，
# 那么只需在redirect()函数中使用url_for()函数生成目标URL即可
from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route("/")
def hi():
    # 重定向到/hello
    return redirect(url_for("hello"))

@app.route("/hello")
def hello():
    pass
