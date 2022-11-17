from flask import Flask, session, redirect

app = Flask(__name__)
app.secret_key = 'allo'


@app.route('/')
def hello_world():
    return 'Hello {}!'.format(session.get('name', 'SOEN287'))


@app.route('/<name>')
def set_name(name):
    session['name'] = name
    return redirect('/')


if __name__ == '__main__':
    app.run()
