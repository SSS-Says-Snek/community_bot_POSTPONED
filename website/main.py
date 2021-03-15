from flask import Flask, render_template
from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, PackageLoader
import discord
client = discord.Client()

env = Environment(loader=PackageLoader('main', 'templates'))
# app = Flask(__name__)
app = Sanic(__name__)

async def user_get():
    guild = client.get_guild(683869900850200581)
    return guild.get_member(753295703077421066).status

@app.route('/', methods=['GET', 'POST'])
async def index(request):
    return html("test work yay")

# @app.route('/index')
# def index_test():
#    print(type(user_get()))
#     return render_template('index.html', status=await user_get())

@app.route('/index')
async def index_test(request, methods=['GET', 'POST']):
    template = env.get_template('index.html')
    html_content = template.render(name=await user_get())
    return html(html_content)

if __name__ == '__main__':
    # host='127.0.0.1'
    app.run(port=8001, debug=True)