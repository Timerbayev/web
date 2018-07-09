from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import Http404
from .models import Question, Answer
from django.core.exceptions import ObjectDoesNotExist


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def post_list(request):
    object1 = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(object1, limit)
    page = paginator.page(page)
    return render(request, 'posts.html', {'paginator': paginator, 'page': page})


def popular(request):
    object1 = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(object1, limit)
    page = paginator.page(page)
    return render(request, 'posts.html', {'paginator': paginator, 'page': page})


def posts(request, slug=1):
    try:
        object2 = Question.objects.new()
        ob = object2.get(id=slug)
        title = ob.title
        text = ob.text
    except ObjectDoesNotExist:
        raise Http404
    try:
        object3 = Answer.answers.filter(author=ob.author)
        answers = object3
    except ObjectDoesNotExist:
        answers = None    # raise Http404
    return render(request, "post.html", {'title': title, 'text': text, 'answers': answers})

# Create your views here.
