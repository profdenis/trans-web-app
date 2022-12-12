import csv
from flask import Flask, render_template, redirect, url_for, request

from forms import ContactForm, ExamplesForm

app = Flask(__name__)
# setting the app's secret key like this is not secure, but for now it's good enough to make it work
app.secret_key = 'allo'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/links')
def links():
    links_list = [('Python', 'https://www.python.org'),
                  ('Flask', 'https://flask.palletsprojects.com/en/2.2.x/'),
                  ('PyCharm', 'https://www.jetbrains.com/pycharm/')]
    return render_template('links.html', links_list=links_list)


@app.route('/documents')
def documents():
    # TODO: put the prefix in the app config dictionary
    prefix = '/static/'
    with open('data/documents.csv') as f:
        doc_list = list(csv.reader(f))[1:]
    return render_template('documents.html', doc_list=doc_list, prefix=prefix)


@app.route('/examples1')
def examples1():
    return render_template('examples1.html')


@app.route('/form_data1', methods=['POST'])
def form_data1():
    return render_template('form_data1.html', form=request.form,
                           checkboxes=request.form.getlist('checkbox_group'))


@app.route('/examples2', methods=['GET', 'POST'])
def examples2():
    form = ExamplesForm()
    if form.validate_on_submit():
        return render_template('form_data1.html', form=request.form,
                               checkboxes=request.form.getlist('checkbox_group'))
    return render_template('examples2.html', form=form)


@app.route('/git')
def assignments():
    return render_template('git.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        with open('data/messages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([form.name.data, form.email.data, form.message.data])
        return redirect(url_for('contact_response', name=form.name.data))
    return render_template('contact.html', form=form)


@app.route('/contact_response/<name>')
def contact_response(name):
    return render_template('contact_response.html', name=name)


if __name__ == '__main__':
    app.run()
