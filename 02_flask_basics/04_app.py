from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('04_index.html',
                           hello=url_for('hello_web_app'),
                           goodbye=url_for('goodbye_web_app'))


@app.route('/hello')
def hello_web_app():
    return '<h1>Hello Web App!</h1>'


@app.route('/goodbye')
def goodbye_web_app():
    return '<h1>Goodbye Web App!</h1>'


if __name__ == '__main__':
    app.run()

