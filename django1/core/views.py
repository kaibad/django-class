from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# this is a  function based view(fbv)
def home_page(request):
    return HttpResponse("Hello Welcome to the newest path")

def contact_page(request):
    return HttpResponse("Contact me ASAP")