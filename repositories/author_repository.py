from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository


def save(author):
    sql = "INSERT INTO authors (author_name) VALUES (%s) RETURNING *"
    values = [author.author_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['author_name'], row['id'] )
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = Author(result['author_name'], result['id'] )
    return author

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

