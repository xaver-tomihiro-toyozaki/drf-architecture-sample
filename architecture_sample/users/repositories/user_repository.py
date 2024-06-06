

from users.models import User


class UserRepository:
  
  def create(self, validated_user):
    return User.objects.create(**validated_user)
  
  def save(self, user: User):
    user.save()
    return user
  
  def save_profile(self, user_profile):
    user_profile.save()
    return user_profile
  
  