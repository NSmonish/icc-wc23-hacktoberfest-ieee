from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from models import Fixtures

#Create a Flask Instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fixtures.db'

#Initialize Database
db = SQLAlchemy(app)
    
class Fixtures(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    time=db.Column(db.String(5))
    day_month=db.Column(db.String(10))
    date=db.Column(db.String(100))
    team_1=db.Column(db.String(200),nullable=False)
    team_2=db.Column(db.String(200),nullable=False)
    venue=db.Column(db.String(200))
    matchNumber=db.Column(db.String(3),nullable=False)
    
    def __repr__ (self):
        return '<matchNumber %r>' % self.venue
    
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
    fixtures = Fixtures(time="14:00",day_month="Friday Oct",date="05/10/23",team_1="New Zealand",team_2="England",venue="Narendra Modi Staduium",matchNumber="1")
    db.session.add(fixtures)
    db.session.commit()
    return render_template('fixtures.html')

@app.route('/Fan_Poll')
def Fan_Poll():
    return render_template('Fan_Poll.html')

if __name__ == "__main__":
    app.run(debug=True)