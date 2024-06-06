
from books.domain.services.loan_service import LoanService
from books.models import Book
from users.models import User
from users.repositories.user_repository import UserRepository

from django.db import transaction

class RentalService:
    def __init__(self, loan_service: LoanService, user_repository: UserRepository):
        self.loan_service = loan_service
        self.user_repository = user_repository
    
    @transaction.atomic
    def rent_book(self, user: User, book: Book):
        # 本を貸し出し
        self.loan_service.loan_book(user, book)
        
        # ユーザのグレードアップ
        user.grade_up_by_pages(book.pages)
        self.user_repository.save(user)
