"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from qa.views import test, post_list, posts, popular, ask, answer, sign, log

urlpatterns = [
    url(r'^question/123/', answer, name='question'),
    url(r'^question/(?P<slug>\w+)/$', posts, name='posts'),
    url(r'^login/.*', log, name='login'),
    url(r'^signup/.*', sign, name='signup'),
    url(r'^ask/.*', ask, name='ask'),
    url(r'^popular/.*', popular, name='popular'),
    url(r'^new/.*', test, name='new'),
    url(r'', post_list, name='post_list'),
     ]#

