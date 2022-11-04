from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("03_index.html")


@app.route('/hello')
def hello_web_app():
    return '<h1>Hello Web App!</h1>'


if __name__ == '__main__':
    app.run()

