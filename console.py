import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Irvine Welsh")
author_repository.save(author1)
author2 = Author("Cormac McCarthy")
author_repository.save(author2)

book1 = Book("Python book", "Computing", author1)
book_repository.save(book1)
book2 = Book("No country for old men", "Fiction", author2)
book_repository.save(book2)

book_repository.select_all()

pdb.set_trace()