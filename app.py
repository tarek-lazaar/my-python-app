import json
from config import Config
from flask import Flask , request , Response

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__ , instance_relative_config=False)
app.config.from_object(Config)
db = SQLAlchemy(app)
#dict of dictionnaries
movie_db = {"1": {"name" : "starwars" , "release_date" : "1998"} ,
            "2":{"name" : "Dune" , "release_date" : "2021"},
            }

class Movies(db.Model):
    id = db.Column('id' , db.Integer , primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_year = db.Column(db.Integer)


@app.route("/")
def home():
    return "Hello world"


@app.route("/hello")
def hello():
    return "<h1> test </h1>"

@app.route("/movie")
def movie():
    #retrieve all movies from Table Movies :
    movie = Movies.query.all() #select * from Movies
    html_response = "<ul>"
    for m in movie:
        html_response += "<li>" + "<a href='/movie/" + str(m.id) + "'>" + m.name + "</a>" + "</li>"
    html_response += "</ul>"
    return html_response

@app.route("/movie/<movie_id>" , methods=["GET"])
def movie_id (movie_id):
    return json.dumps(movie_db[movie_id])





if __name__ == "__main__" :
    app.run(debug=True , host="127.0.0.1")
