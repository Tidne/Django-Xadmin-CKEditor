from . import views
from django.urls import path

name='app'

urlpatterns = [
        path('',views.index,name='index'),
        path('blog/<str:name>',views.blog,name='blog'),
]