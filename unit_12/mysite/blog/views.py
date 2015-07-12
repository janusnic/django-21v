from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#  home_page = None
def home_page(request):
    return HttpResponse('<html><title>Blog lists</title></html>')

# "You must be joking!" I can hear you say.