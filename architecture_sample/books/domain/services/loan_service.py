
from books.models import Book, Loan
from users.models import User


class LoanService:
    def __init__(self, loan_repository, book_repository):
        self.loan_repository = loan_repository
        self.book_repository = book_repository
        
    def loan_book(self, user: User, book: Book):
        loan = Loan(user=user, book=book)
        self.loan_repository.create(loan)
        self.book_repository.save(book.decrement_stock())
        