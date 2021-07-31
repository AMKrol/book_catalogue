from models import db


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
