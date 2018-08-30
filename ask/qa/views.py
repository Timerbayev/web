from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import Question, Answer
from django.core.exceptions import ObjectDoesNotExist
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate, login


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def salt_and_hash(password):
    hasher = PBKDF2PasswordHasher()
    password_ = hasher.encode(password=password, salt='salt', iterations=20)
    return password_


def session_user(request):
    if request.user is not None:
        user = User.objects.get(username=request.user)
        return user


def post_list(request):
    object1 = Question.objects.all()
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
        object3 = Answer.objects.filter(author=ob.author)
        answers = object3
    except ObjectDoesNotExist:
        answers = None
    return render(request, "post.html", {'title': title, 'text': text, 'answers': answers})


def ask(request):
    if request.method == "POST":
        AskForm(initial={'author': request.user})
        form = AskForm(request.POST)
        print("valid - ", form.is_valid(), form, "QueryDict", request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect('/question/123/')
    else:
        try:
            form = AskForm(initial={'author': request.user})  # initial={'author': request.user}
        except ObjectDoesNotExist:
            form = AskForm()
    return render(request, 'ask.html', {'form': form})


def answer(request):
    if request.method == "POST":
        AnswerForm(initial={'author': request.user})
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer1 = form.save()
            answer1.author = request.user
            answer1.save()
            return HttpResponseRedirect('/question/123/')
    else:
        try:
            question = Question.objects.order_by('-id').first()
            form = AnswerForm(initial={'author': request.user, 'question': Question.objects.order_by('-id').get(id=question.id)})
        except ObjectDoesNotExist:
            form = AnswerForm()
    return render(request, 'answer.html', {'form': form})


def sign(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            form = form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'sign.html', {'form': form})


def log(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Your login is wrong'
                form = LoginForm()
                return render(request, 'login.html', {'error': error, 'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



