from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    links = [url_for('hello_web_app'), url_for('hello_name', name='Denis'), url_for('goodbye_web_app')]
    return render_template('05_index.html', links=links)


@app.route('/hello')
def hello_web_app():
    return '<h1>Hello Web App!</h1>'


@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello_name.html', name=name)


@app.route('/goodbye')
def goodbye_web_app():
    return '<h1>Goodbye Web App!</h1>'


if __name__ == '__main__':
    app.run()
