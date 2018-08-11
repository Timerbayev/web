from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name="username")

    def clean_text(self):
        text = self.cleaned_data["text"]
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.new(), to_field_name="id")
    author = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name="username")

    def clean_text(self):
        text = self.cleaned_data["text"]
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        return username

    def save(self):
        hasher = PBKDF2PasswordHasher()
        self.cleaned_data['password'] = hasher.encode(password=self.cleaned_data['password'], salt='salt', iterations=20)
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)