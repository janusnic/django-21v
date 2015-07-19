# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime 

from django.views.generic import TemplateView

# Create your views here.
#  home_page = None
class MyStruct(object): 
	pass 

def home_page(request):
    return HttpResponse('<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')

def index(request):
	c = MyStruct()
	c.company = 'Cool Star' 
	c.title = 'Cool Star Blog' 
	c.author_name = 'Jhon Smith' 
	c.pub_date = datetime.datetime.now() 
	c.article_list = [{'title':'Title1','text':'text1'},{'title':'Title2','text':'text2'},{'title':'Title3','text':'text3'}]
	c.boldmessage = "Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context"
	c.text = 'Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ text|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.'
	return render(request, 'blog/index.html',  c.__dict__)

class AboutView(TemplateView):
    template_name = "about.html"