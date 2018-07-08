from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import Http404
from .models import Question, Answer


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
    args = {}
    try:
        object2 = Question.objects.new()
        ob = object2.get(id=slug)
        args['title'] = ob.title
        args['text'] = ob.text
    except Question.DoesNotExist:
        raise Http404
    try:
        object3 = Answer.objects.get(author=ob.author)
        args['answer'] = object3.text
    except Answer.DoesNotExist:
        args['answer'] = None    # raise Http404
    return render(request, "post.html", args)

# Create your views here.
