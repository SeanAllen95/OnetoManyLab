from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books_list = book_repository.select_all()
    print(books_list)
    return render_template("books/index.html", title = 'Home', books = books_list)

# @books_blueprint.route("/books/new", methods=['GET'])
# def new_book():
#     books = book_repository.select_all()
#     return render_template("books/new.html", all_books = books)