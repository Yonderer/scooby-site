"""Flask App Project."""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


if __name__ == '__main__':
    app.run()
