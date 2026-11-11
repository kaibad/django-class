from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Blog, Post
from django.db.models import Q

# Create your views here.

# this is a  function based view(fbv)
def home_page(request):
    print("Request to Home page")
    # print("request.method",request.method)
    # print("request.pOST",request.POST)
    # print("request.GET",request.GET)
    search_keyword = request.GET.get("q","")
    # this below is a ORM which is django pros
    if search_keyword =="":
        blogs = Blog.objects.all().order_by('-created_at') # - is negative this means descending
    else:
        # blogs = Blog.objects.filter(title__icontains=search_keyword).order_by('-created_at')
        blogs = Blog.objects.filter(
            Q(title__icontains=search_keyword) |
            Q(content__icontains=search_keyword)
        ).order_by('-created_at')
    return render(request,'core/home.html',{'blogs':blogs})

    # return render(request,"core/home.html")

def contact_page(request):
    print("Request reaches here")
    return render(request,"core/contact.html")

def create_post(request):
    # print(request.method,request.POST)
    form_data = request.POST
    try:
        Post.objects.create(caption = form_data.get("caption"),user = request.user)
    except Exception as e:
        print("Post not created ", e)
        return HttpResponse("Post creation Failed")
    else:
        print("Post creation successfully")
        return HttpResponse("Post created successfully")

def create_blog(request):
    form_data = request.POST
    # print(request.method,form_data)
    try:
        Blog.objects.create(title = form_data.get("title"),content = form_data.get("content"))
    except Exception as e:
        print("Blog not created ", e)
        return HttpResponse("Post creation Failed")
    else:
        print("Blog creation successfully")
        return redirect("home_page_url")

def read_blog(request,id):
    blog = Blog.objects.get(pk=id)
    return render(request,"core/blog-single.html",{'blog':blog})

def delete_blog(request,id):
    blog = Blog.objects.get(pk=id)
    return render(request,"core/blog-delete.html",{'blog':blog})

def confirm_delete_blog(request):
    # print(request.POST)
    blog_id = request.POST.get("blog-id")
    count , _ = Blog.objects.get(pk=blog_id).delete()
    print(f"{count} items deleted.")
    return redirect("home_page_url")

def update_blog(request,id):
    if request.method == 'POST':
        blog_id = request.POST.get("blog-id")
        updated_title = request.POST.get("title")
        updated_desc = request.POST.get("content")

        blog_to_update = Blog.objects.get(pk=blog_id)
        blog_to_update.title = updated_title
        blog_to_update.content = updated_desc

        blog_to_update.save()
        return redirect("home_page_url")

    blog = Blog.objects.get(pk=id)
    return render(request,"core/blog-update.html",{'blog':blog})
