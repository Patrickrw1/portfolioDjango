from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('blog.html', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),   
]
