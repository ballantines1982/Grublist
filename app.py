from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Meal(db.Models):
    id = db.Column(db.Interger, primary_key=True)
    meal = db.Column(db.String(100))




@app.route('/')
def hello():
    return "Flask App"


if __name__ == "__main__":
    app.run()