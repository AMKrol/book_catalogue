from models import app, db
from models.book import Book
from models.authors import Authors
from models.status import Status
from flask import Flask, render_template, request, flash
from flask import redirect, url_for
from book_catalogueSQLLite import CatalogueSQLLite
from forms import AddBookForm


book_db = CatalogueSQLLite()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Authors": Authors,
        "Status": Status
    }


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/book_list")
def show_book_list():
    form = AddBookForm()
    book_list = book_db.get_all_book()
    return render_template("book_list.html", book_list=book_list, form=form)


@app.route("/add_book", methods=["POST"])
def add_book():
    data = request.form
    book_db.create(data)

    return redirect(url_for("show_book_list"))
