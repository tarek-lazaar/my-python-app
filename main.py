import json

from flask import Flask , request , Response



app = Flask(__name__)

#dict of dictionnaries
movie_db = {"1": {"name" : "starwars" , "release_date" : "1998"} ,
            "2":{"name" : "Dune" , "release_date" : "2021"},
            }


@app.route("/")
def home():
    return "Hello world"


@app.route("/hello")
def hello():
    return "<h1> test </h1>"

@app.route("/movie")
def movie():
    return json.dumps(movie_db)

@app.route("/movie/<movie_id>" , methods=["GET"])
def movie_id (movie_id):
    return json.dumps(movie_db[movie_id])





if __name__ == "__main__" :
    app.run(debug=True , host="127.0.0.1")
