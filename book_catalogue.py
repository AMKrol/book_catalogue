from models import app, db
from models.book import Book
from models.authors import Authors
from models.rent import Status

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Authors": Authors,
       "Status": Status
   }