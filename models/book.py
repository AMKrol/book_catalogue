from models import db

author = db.Table('author',
    db.Column("book_id", db.Integer, db.ForeignKey("book.book_id")),
    db.Column("authors_id", db.Integer, db.ForeignKey("authors.authors_id"))
)
class Book(db.Model):
   book_id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   release_year = db.Column(db.String(200))
   status = db.Column(db.String(128))
   authors = db.relationship("Authors",
                    secondary="author",
                    backref=db.backref("book_title", lazy="dynamic"))

   def __str__(self):
       return f"<User {self.username}>"

class Authors(db.Model):
   authors_id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.Text)
   second_name = db.Column(db.Text)

   def __str__(self):
       return f"<Post {self.id} {self.body[:50]} ...>"