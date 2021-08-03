from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Title"})
    authors = StringField('Authors', validators=[DataRequired()], render_kw={"placeholder": "Authors, separate by comma"})
    release_year = StringField('Release Year', validators=[DataRequired()], render_kw={"placeholder": "Release year"})
    status = SelectField(u'Field name', choices = ["borrowed", "on stock"], validators = [DataRequired()])
