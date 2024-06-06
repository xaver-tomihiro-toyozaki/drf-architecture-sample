from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    
    def grade_up_by_pages(self, pages: int):
        return self.profile.grade_up_by_pages(pages)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0)
    pages_read = models.IntegerField(default=0)
    grade = models.CharField(max_length=20, default='Bronze')
    
    def grade_up_by_pages(self, pages: int):
        self.pages_read += pages
        if self.pages_read >= 500:
            self.grade = 'Silver'
        if self.pages_read >= 1000:
            self.grade = 'Gold'
        if self.pages_read >= 2000:
            self.grade = 'Platinum'
        if self.pages_read >= 5000:
            self.grade = 'Diamond'
        return self.grade