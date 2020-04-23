import os

from flask import Flask, session
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



@app.route("/")
def index():
    books = db.execute("SELECT * FROM books").fetchall() 
    return render_template('index.html', books=books)



@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        query = request.form.get("input-search")
       
    if query is None:
        return print("Search field can not be empty!")
        
    else:
        result = db.execute("SELECT * FROM books WHERE LOWER(isbn) LIKE :query OR LOWER(title) LIKE :query OR LOWER(author) LIKE :query", {"query": "%" + query.lower() + "%"}).fetchall()

        return render_template("results.html", result=result)


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