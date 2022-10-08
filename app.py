from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template('homepage.html')


@app.route('/about')
def index_about():
    return render_template('about.html')


@app.route('/services')
def index_services():
    return render_template('services.html')


@app.route('/work')
def index_work():
    return render_template('work.html')


@app.route('/contacts')
def index_contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
