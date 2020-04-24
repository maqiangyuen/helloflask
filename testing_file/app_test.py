"""
Flask会自动探测程序实例，自动探测存在下面这些规则：
    ❑ 寻找app.py和wsgi.py模块，并从中寻找名为app或application的程序实例。
    ❑ 从环境变量FLASK_APP对应的值寻找名为app或application的程序实例。
    ❑ 如果安装了python-dotenv，那么在使用flask run或其他命令时会使用它自动从.
       flaskenv文件和.env文件中加载环境变量。
    如果安装了python-dotenv，那么在使用flask run或其他命令时会使用它自动从.
    flaskenv文件和.env文件中加载环境变量。
Flask在加载环境变量的优先级是：
    手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量
"""



from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world</h1>"