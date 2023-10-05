from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Create a Flask Instance
app = Flask(__name__)

#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fixtures.db'

#Initialize Database
db = SQLAlchemy(app)

#Create Model
class Fixtures(db.Model):
    time = db.Column(db.String(5))
    day_month = db.Column(db.String(10))
    date = db.Column(db.String(10))
    home_team = db.Column(db.String(200), nullable=False)
    away_team = db.Column(db.String(200), nullable=False)
    venue = db.Column(db.String(200))
    matchNumber = db.Column(db.Integer, primary_key=True)
    roundNumber = db.Column(db.Integer, nullable=False)
    
    def __repr__ (self):
        return '<matchNumber %r>' % self.venue
    
from app import Fixtures

with app.app_context():
    db.create_all()
    

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
