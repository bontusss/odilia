from email.policy import default
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
class Word(models.Model):
    name = models.CharField(help_text="The name of the word", max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 


class Definition(models.Model):
    meaning = models.TextField(help_text="Add the meaning of the selected word")
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"Definition for {self.word} by {self.author}"









