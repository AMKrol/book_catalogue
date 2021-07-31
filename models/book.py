from models import db

author = db.Table('author',
                  db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
                  db.Column("authors_id", db.Integer,
                            db.ForeignKey("authors.id"))
                  )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    release_year = db.Column(db.String(200))
    status = db.relationship("Status", backref="book", lazy="dynamic")
    authors = db.relationship("Authors",
                              secondary="author",
                              backref=db.backref("book_title", lazy="dynamic"))

    def __str__(self):
        return f"<User {self.title}>"
