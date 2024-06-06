from django.db import models

from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    pages = models.IntegerField()
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def decrement_stock(self):
        self.stock -= 1
        return self


class Loan(models.Model):
    book = models.ForeignKey(Book, related_name='loans', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)