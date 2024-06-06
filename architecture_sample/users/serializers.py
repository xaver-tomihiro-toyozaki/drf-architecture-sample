

from users.models import User
from rest_framework import serializers

from users.services.user_service import UserService

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        user_service: UserService = self.context['user_service']
        # 初回ユーザ作成時にビジネスロジックを必要とするのでserviceに処理を委譲
        return user_service.create_user(validated_data)
    
