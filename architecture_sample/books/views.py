from django.shortcuts import render
from requests import Response

from books.domain.services.loan_service import LoanService
from books.models import Book
from books.repositories.loan_repository import LoanRepository
from books.serializers import BookSerializer

from rest_framework import viewsets
from rest_framework.decorators import action

from books.services.rental_service import RentalService

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        # loan_serviceにLoanRepositoryを注入
        loan_service = LoanService(LoanRepository())
        # user_serviceにUserRepositoryを注入
        rental_service = RentalService(loan_service)
        # contextにuser_serviceを追加(意図としては注入)
        context['user_service'] = rental_service
        self.rental_service = rental_service
        return context

    @action(detail=True, methods=['post'])
    def rent(self, request, pk=None):
        self.rental_service.rent_book(request.user, self.get_object())
        return Response({'status': 'ok'})