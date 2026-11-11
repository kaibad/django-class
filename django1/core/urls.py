from django.urls import path
from core import views


urlpatterns = [
    path('',views.home_page,name="home_page_url" ),
    path('home/',views.home_page ),
    path('blog/write/',views.create_blog,name="create_blog_post_url"),
    path('blog/read/<id>/',views.read_blog,name="read_blog_url"),
    path('blog/delete/<id>/',views.delete_blog,name="delete_blog_url"),
    path('blog/delete/',views.confirm_delete_blog,name="confirm_delete_blog_url"),
    path('blog/update/<id>/',views.update_blog,name="update_blog_url"),

    path('contact/',views.contact_page),
]
