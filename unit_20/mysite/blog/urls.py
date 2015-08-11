"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    
    # url(r'^$', views.home_page, name='blog'),
    url(r'^$', views.index, name='blog'),
    url(r'^categories/', 'blog.views.categories'),
    url(r'^category/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^login/$', 'blog.views.user_login', name='login'),
    url(r'^restricted/', 'blog.views.restricted', name='restricted'),
    url(r'^logout/$', 'blog.views.user_logout', name='logout'),
    url(r"^month/(\d+)/(\d+)/$", "blog.views.month"),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    url(r'^pages/(?P<pageslug>.*)/$', 'blog.views.page'),
    url(r'^goto/$', 'blog.views.track_url', name='goto'),

]
