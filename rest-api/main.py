from flask import Flask, make_response, redirect, request
from dataclasses import asdict, dataclass
import json

@dataclass
class Movie:
  title: str
  release_year: int
  director: str

trilogy: list[Movie] = [
  Movie("Spider-Man", 2002, "Sam Raimi"),
  Movie("Spider-Man 2", 2004, "Sam Raimi"),
  Movie("Spider-Man 3", 2007, "Sam Raimi"),
]

app = Flask(__name__)

@app.route("/")
def hello_world():
  return """<p>Welcome to the Original Spiderman Trilogy Movie API!</p> 
  <img src="https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg" />"""


@app.route("/spiderman-trilogy")
def movies():
  return trilogy


@app.route("/spiderman-trilogy/<int:index>")
def movie(index):
  return trilogy[index - 1] if 0 < index < len(trilogy) + 1 else redirect('https://http.cat/404')


@app.post("/spiderman-trilogy")
def add_movie():
  if request.data == b'' or request.data == None:
    return redirect('https://http.cat/400')

  try:
    mov = json.loads(request.data)
    # just leared about dict destructuring, that's crazy
    trilogy.append(Movie(**mov))
    return make_response(trilogy, 201)
  except Exception as e:
    return internal_server_error(e)


@app.delete("/spiderman-trilogy/<int:index>")
def delete_movie(index: int):
  try:
    popped = asdict(trilogy.pop(index - 1))
    return make_response(popped, 200)
  except Exception as e:
    return internal_server_error(e)


@app.errorhandler(404)
def page_not_found(error):
  return redirect('https://http.cat/404')


@app.errorhandler(500)
def internal_server_error(error):
  return redirect('https://http.cat/500')
