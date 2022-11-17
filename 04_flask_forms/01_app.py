import csv

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def contact_form():
    return render_template('01_contact_form.html')


@app.route('/form2')
def contact_form2():
    return render_template('02_contact_form.html')


@app.route('/contact_form', methods=['POST'])
def handle_contact_form():
    # we should normally validate the submitted form data before using it
    # by default, the template rendering will be considered unsafe, so the data will be escaped
    return render_template('03_contact_response.html', data=request.form)


@app.route('/contact_form2', methods=['POST'])
def handle_contact_form2():
    with open('data/messages.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([request.form['name'], request.form['email'], request.form['message']])
    return render_template('03_contact_response.html', data=request.form)


if __name__ == '__main__':
    app.run()
