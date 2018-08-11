from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def last(self):
        return self.order_by('-id').last()

    def popular(self):
        return self.order_by('-rating')


class Question (models.Model):
    objects1 = models.Manager()
    objects = QuestionManager()
    title = models.CharField(max_length=50, blank=True, null=True, default=None)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return str(self.id)


class Answer (models.Model):
    objects = models.Manager()
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text


class Session(models.Model):
    objects = models.Manager()
    key = models.CharField(unique=True, max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    expires = models.DateTimeField()

    def __str__(self):
        return self.key
