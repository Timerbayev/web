from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

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
    #author = forms.CharField(max_length=100, widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data["text"]
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer