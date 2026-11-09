from django.shortcuts import render
from .models import Note

# Create your views here.

# this is a  function based view(fbv)
def home_page(request):
    print("Request to Home page")
    # this below is a ORM which is django pros
    notes = Note.objects.all()
    return render(request,'core/home.html',{'notes':notes})

    # return render(request,"core/home.html")

def contact_page(request):
    print("Request reaches here")
    return render(request,"core/contact.html")