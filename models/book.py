from datetime import datetime
from models import db

association_table = db.Table('association',
    db.Column('book_id', db.ForeignKey('book.id')),
    db.Column('author_id', db.ForeignKey('author.id'))
)

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), index=True, unique=True)
   release_year = db.Column(db.String(200), index=True, unique=True)
   status = db.Column(db.String(128))
   authors = db.relationship("Authors", secondary=association_table,
        back_populates="book")

   def __str__(self):
       return f"<User {self.username}>"

class Authors(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.Text)
   second_name = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('Book.id'))
   books = db.relationship(
        "Book",
        secondary=association_table,
        back_populates="authors")

   def __str__(self):
       return f"<Post {self.id} {self.body[:50]} ...>"