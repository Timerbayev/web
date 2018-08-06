from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import Question, Answer, Session
from django.core.exceptions import ObjectDoesNotExist
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
import datetime
import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher

def generate_long_random_key():
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1',  '2', '3', '4', '5', '6']
    password = []
    for i in range(10):
        password.append(random.choice(array))
    return "".join(password)


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def salt_and_hash(password):
    hasher = PBKDF2PasswordHasher()
    password_ = hasher.encode(password=password, salt='salt', iterations=20)
    return password_


def session_user(request):
    sessionid = request.COOKIES.get('sessionid')
    session = Session.objects.get(key=sessionid, expires__gt=datetime.datetime.now())
    request.session = session
    return session.user


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
        object3 = Answer.objects.filter(author=ob.author)
        answers = object3
    except ObjectDoesNotExist:
        answers = None    # raise Http404
    return render(request, "post.html", {'title': title, 'text': text, 'answers': answers})


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        request.user = session_user(request)
        form._user = request.user
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/question/123/')
    else:
        if session_user(request) is not  None:
            form = AskForm(initial={'author': session_user(request)})
        else:
            form = AskForm()
    return render(request, 'ask.html', {'form': form})


def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        request.user = session_user(request)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/question/123/')
    else:
        print(session_user(request),  'Session_User')
        try:
            question = Question.objects.order_by('-id').first()
            form = AnswerForm(initial={'author': session_user(request), 'question': Question.objects.order_by('-id').get(id=question.id)})
        except ObjectDoesNotExist:
            form = AnswerForm()
    return render(request, 'answer.html', {'form': form})


def sign(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'sign.html', {'form': form})


def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None
    session = Session()
    session.key = generate_long_random_key()
    session.user = user
    session.expires = datetime.datetime.now() + datetime.timedelta(days=1)
    session.save()
    return session.key


def log(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('continue', '/')
        sessionid = do_login(username, password)
        if sessionid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid, httponly=True,
                                expires=datetime.datetime.now()+datetime.timedelta(days=1))
            return response
        else:
            error = u'Login is wrong / пароль'

    else:
        form = LoginForm()
    return render(request, 'login.html', {'error': error, 'form': form})



# Create your views here.
