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
            a = Authors(first_name=aut[0], second_name=aut[1])
            db.session.add(a)
            a.book_title.append(book)

        status_db = Status(status_name=status, book=book)
        db.session.add(status_db)
        db.session.commit()

    def update(self):
        pass

    def get_all_book(self):
        return Book.query.all()

    def get_all_authors(self):
        return Authors.query.all()

    def delete_author(self, author_id):
        author = Authors.query.get(author_id)
        db.session.delete(author)
        db.session.commit()
