from models import authors
from models.book import Book
from models.status import Status
from models.authors import Authors
from models import db


class CatalogueSQLLite():
    def __init__(self):
        pass

    def create(self, data):
        title = data.get("title")
        authors = data.get("authors")
        release_year = data.get("release_year")
        status = data.get("status")

        book = Book(title=title, release_year=release_year)
        db.session.add(book)

        authors_list = authors.split(", ")
        for autor in authors_list:
            aut = autor.split(" ")
            exists = db.session.query(Authors.id).filter_by(
                first_name=aut[0], second_name=aut[1]).first() is not None
            a = ""
            if exists:
                a = db.session.query(Authors.id).filter_by(
                    first_name=aut[0], second_name=aut[1]).first()
                a = Authors.query.get(a)
            else:
                a = Authors(first_name=aut[0], second_name=aut[1])
                db.session.add(a)
            a.book_title.append(book)

        status_db = Status(status_name=status, book=book)
        db.session.add(status_db)
        db.session.commit()

    def update(self):
        pass

    def get_info_for_update(self, book_id):
        book = Book.query.get(book_id)

        authors_list = []
        for author in book.authors:
            authors_list.append(author.first_name + " " + author.second_name)
        authors_list = ", ".join(authors_list)

        if book.status.first().status_name == "borrowed":
            status = "borrowed"
        else:
            status = "on stock"

        return [book.title, authors_list, book.release_year, status]

    def get_all_book(self):
        return Book.query.all()

    def get_all_authors(self):
        return Authors.query.all()

    def delete_author(self, author_id):
        author = Authors.query.get(author_id)
        db.session.delete(author)
        db.session.commit()

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
