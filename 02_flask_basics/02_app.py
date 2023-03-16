from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f'<a href="{url_for("hello_web_app")}">Hello Web App</a>'
    # return '<a href="/hello">Hello Web App</a>'


@app.route('/hello')
def hello_web_app():
    return '<h1>Hello Web App!</h1>'


if __name__ == '__main__':
    app.run()

