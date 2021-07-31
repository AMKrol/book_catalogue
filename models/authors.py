from models import db


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    second_name = db.Column(db.Text)

    def __str__(self):
        return f"<Author {self.first_name} {self.second_name} ...>"
