from flask import Flask

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return '<h1>Hello Web App!</h1>'


if __name__ == '__main__':
    app.run()
