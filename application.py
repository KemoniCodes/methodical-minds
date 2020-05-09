import os
import requests


from flask import Flask, session
import urllib3
import json
from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from models import *

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
key = os.getenv("KEY")




@app.route("/")
def index():
    books = db.execute("SELECT * FROM books").fetchall()
    if books is None:
        return render_template("noResults.html")
    return render_template('index.html', books=books)


@app.route("/login")
def login():
       return render_template("login.html")

@app.route("/loggedIn", methods=["GET", "POST"])
def loggedIn():
    if request.method == "GET":
        return redirect("/")
    return render_template('loggedIn.html')

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/search", methods=["GET","POST"])
def search():
    query = []

    if request.method == "GET":
        return render_template("search.html")
    
    query = request.form.get("input-search")
  

    if not query:
        return render_template("noResults.html")
   

    result = db.execute("SELECT * FROM books WHERE LOWER(isbn) LIKE :query OR LOWER(title) LIKE :query OR LOWER(author) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall()

    if not db.execute("SELECT * FROM books WHERE LOWER(isbn) LIKE :query OR LOWER(title) LIKE :query OR LOWER(author) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall() :
        return render_template("noResults.html", result=result)

    return render_template("results.html", result=result)


@app.route('/book/<string:isbn>', methods = ['POST','GET'])
def book(isbn):
    #import columns from database 
    res = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    return render_template("bookPage.html", isbn = isbn, title = res.title, author = res.author)
    r = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "74JSBvyeNTPrZxlcIOHw", "isbns": isbn})
    if r.status_code != 200:
      raise ValueError
    # return render_template("bookPage.html", isbn = isbn, title = title, author = author)

    




# @app.route('/books/<string:isbn>', methods=["GET","POST"])

# import urllib3
# import json
# import requests

# def book(isbn):
# import requests
# url= requests.get("https://www.goodreads.com/book/isbn/ISBN?format=FORMAT", params={"format":"xml", "key": "74JSBvyeNTPrZxlcIOHw", "isbn": "1632168146" })
# print(url)



# import requests
# res = requests.get("https://www.goodreads.com/book/isbn/ISBN?format=FORMAT", params={"key": "74JSBvyeNTPrZxlcIOHw", "isbns": "9781632168146"})
# print(res())

# import requests
# res = requests.get("https://www.goodreads.com/book/show.FORMAT", params={"format": "json", "key": "74JSBvyeNTPrZxlcIOHw", "id": "isbns": "9781632168146"}) 