# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/hi/<int:year>", methods=["GET", "POST"])
# def hi(year):
#     return "<h1>Hello world! Welcome to {}</h1>".format(year)


# 在用法上唯一特别的是any转换器，
# 你需要在转换器后添加括号来给出可选值，
# 即“<any(value1，value2，...):变量名>”

# 在浏览器中访问http://localhost:5000/colors/<color>时，
# 如果将<color>部分替换为any转换器中设置的可选值以外的任意字符，
# 均会获得404错误响应

from flask import Flask

app = Flask(__name__)

@app.route("/colors/<any(blue, white, red): color>", methods=["GET", "POST"])
def three_colors(color):
    return "<p>Love is parient and kind. " \
           "Love is not jealous or boastful or proud or rude.</p>"