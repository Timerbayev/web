from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')

# Create your models here.
class Question (models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50, blank=True, null=True, default=None)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

class Answer (models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


# Create your models here.
