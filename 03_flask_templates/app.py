import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/documents')
def documents():
    # TODO: put the prefix in the app config dictionary
    prefix = '/static/'
    with open('data/documents.csv') as f:
        doc_list = list(csv.reader(f))[1:]
    return render_template('documents.html', doc_list=doc_list, prefix=prefix)


@app.route('/links')
def links():
    # prefix = '/static/'
    links_list = [('Python', 'https://www.python.org'),
                  ('Flask', 'https://flask.palletsprojects.com/en/2.2.x/'),
                  ('PyCharm', 'https://www.jetbrains.com/pycharm/')]
    return render_template('links.html', links_list=links_list)


@app.route('/git')
def assignments():
    return render_template('git.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/simple')
def simple():
    return render_template('simple.html')


@app.route('/sub')
def sub():
    return render_template('sub.html')


if __name__ == '__main__':
    app.run()
