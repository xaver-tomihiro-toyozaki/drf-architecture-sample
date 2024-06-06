
from django.db import transaction

from users.models import UserProfile
from users.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
  
    @transaction.atomic
    def create_user(self, validated_data):
        # 初回入会特典で100ポイント付与
        user = self.user_repository.create(validated_data)
        first_enrollment_point = 100
        user_profile = UserProfile(user, points=first_enrollment_point)
        self.user_repository.save_profile(user_profile)
        return user