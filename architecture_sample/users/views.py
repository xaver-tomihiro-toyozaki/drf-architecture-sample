from django.shortcuts import render

from users.models import User
from users.repositories.user_repository import UserRepository
from users.serializers import UserSerializer
from users.services.user_service import UserService

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # user_serviceにUserRepositoryを注入
        user_service = UserService(UserRepository())
        # contextにuser_serviceを追加(意図的には注入)
        context['user_service'] = user_service
        return context