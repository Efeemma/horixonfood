
from django.urls import path, include
from .views import *
app_name="appusers"



urlpatterns = [ 
    path('',index,name='index' ),
    path('menu',menu,name='menu' ),
    path('reservation',reservation,name='reservation' ),
    path('gallery',gallery,name='gallery' ),
    path('contact',contact,name='contact' ),
    path('about',about,name='about' ),
]