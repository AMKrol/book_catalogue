from models import app, db
from models.book import Book, Authors

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Authors": Authors
   }