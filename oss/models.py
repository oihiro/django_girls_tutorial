from django.db import models
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

