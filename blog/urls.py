from django.urls import path
from .views import homePage,aboutPage

urlpatterns = [
    path('',homePage,name = 'blog-home'),
    path('about/',aboutPage,name = 'blog-about'),
]