from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!!!!!!!!!!!!'


@app.route('/index')
def index():
    return render_template('index.html', title='some variable value')


@app.route('/another')
def another():
    return render_template('another.html', title='another')


if __name__ == '__main__':
    app.run()
