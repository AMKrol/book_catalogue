from os import stat
from re import T

from sqlalchemy.sql.elements import BinaryExpression
from models.book import Book, author
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

    def update(self, data):
        book = Book.query.get(data.get("book_id"))

        new_authors_list = data.get("authors")

        old_book_authors = []
        for author in book.authors:
            old_book_authors.append(author.first_name + " " + author.second_name)
        old_book_authors = ", ".join(old_book_authors)

        if not all([data.get("title") == book.title, 
            book.release_year == data.get("release_year"),
            new_authors_list == old_book_authors,
            data.get("status") == book.status.first().status_name]):
            book.title = data.get("title")

            status_db = db.session.query(Status.id).filter_by(
                        book_id=data.get("book_id")).first()
            print(status_db)
            status_db = Status.query.get(status_db)
            print(status_db)
            status_db.status_name = data.get("status")
            book.status.append(status_db)

            book.release_year = data.get("release_year")

            new_authors_list_split = new_authors_list.split(", ")
            old_book_authors_split = old_book_authors.split(", ")

            new_authors_list_split_as_set = set(new_authors_list_split)
            old_book_authors_split_as_set = set(old_book_authors_split)

            intersect_authors_list = list(old_book_authors_split_as_set.intersection(new_authors_list_split_as_set))

            author_list_to_add = new_authors_list_split
            for aut in intersect_authors_list:
                author_list_to_add.remove(aut)
            for aut in old_book_authors_split:
                try:
                    author_list_to_add.remove(aut)
                except:
                    pass

            author_list_to_remove = old_book_authors_split
            for aut in intersect_authors_list:
                author_list_to_remove.remove(aut)
            for aut in new_authors_list:
                try:
                    author_list_to_remove.remove(aut)
                except:
                    pass
            
            for aut in author_list_to_add:
                aut = aut.split(" ")
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

            for aut in author_list_to_remove:
                aut = aut.split(" ")
                author = db.session.query(Authors.id).filter_by(
                        first_name=aut[0], second_name=aut[1]).first()
                author = Authors.query.get(author)
                book.authors.remove(author)

            db.session.commit()

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
        author.hidden = True
        db.session.commit()

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        book.hidden = True
        db.session.commit()
