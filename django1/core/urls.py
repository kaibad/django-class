from django.urls import path
from core import views


urlpatterns = [
    path('',views.home_page ),
    path('home/',views.home_page ),
    path('contact/',views.contact_page),
]


