from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')

if __name__ == "__main__":
    app.run(debug=True)