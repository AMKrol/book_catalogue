from models import app, db
from models.book import Book
from models.authors import Authors
from models.rent import Status
from flask import Flask, render_template, request, flash
from flask import redirect, url_for

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Authors": Authors,
       "Status": Status
   }


@app.route("/")
def homepage():
    return render_template("homepage.html")


