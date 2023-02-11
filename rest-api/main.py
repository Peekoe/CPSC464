from flask import Flask, redirect

trilogy = [
  { "title": "Spider-Man",   "release-year": 2002, "director": "Sam Raimi" },
  { "title": "Spider-Man 2", "release-year": 2004, "director": "Sam Raimi" },
  { "title": "Spider-Man 3", "release-year": 2007, "director": "Sam Raimi" }
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
  return trilogy[index - 1] if 0 < index < 4 else redirect('https://http.cat/404')


@app.errorhandler(404)
def page_not_found(error):
  return redirect('https://http.cat/404')


@app.errorhandler(500)
def internal_server_error(error):
  return redirect('https://http.cat/500')
