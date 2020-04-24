"""
通过创建任意一个函数，
并为其添加app.cli.command()装饰器，
我们就可以注册一个flask命令

函数的名称即为命令名称，这里注册的命令即hello
可以使用flask hello命令来触发函数

作为替代，也可以在app.cli.command()装饰器中传入参数来设置命令名称
"""


import click
from flask import Flask

app = Flask(__name__)

@app.cli.command()
def hello():
    click.echo("Hello Human")