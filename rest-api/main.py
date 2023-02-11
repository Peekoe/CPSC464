from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return """<p>Welcome to the Original Spiderman Trilogy Movie API!</p> 
  <img src="https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg" />"""


@app.route("/movies")
def movies():
  return [
    { "title": "Spider-Man",   "release-year": 2002, "director": "Sam Raimi" },
    { "title": "Spider-Man 2", "release-year": 2004, "director": "Sam Raimi" },
    { "title": "Spider-Man 3", "release-year": 2007, "director": "Sam Raimi" }
  ]
