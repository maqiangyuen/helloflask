from flask import Flask, abort

# abort()函数前不需要使用return语句，
# 但一旦abort()函数被调用，
# abort()函数之后的代码将不会被执行
app = Flask(__name__)
@app.route("/404")
def wrong_url():
    abort(404)

