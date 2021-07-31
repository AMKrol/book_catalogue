from models import db

author = db.Table('author',
    db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
    db.Column("authors_id", db.Integer, db.ForeignKey("authors.id"))
)
class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   release_year = db.Column(db.String(200))
   aaaa = db.relationship("Status", backref="stat", lazy="dynamic")
   authors = db.relationship("Authors",
                    secondary="author",
                    backref=db.backref("book_title", lazy="dynamic"))

   def __str__(self):
       return f"<User {self.title}>"

class Authors(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.Text)
   second_name = db.Column(db.Text)

   def __str__(self):
       return f"<Author {self.first_name} {self.second_name} ...>"

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
