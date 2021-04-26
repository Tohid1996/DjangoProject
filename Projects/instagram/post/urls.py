from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('hello/', views.index, name='hello'),
    path('posts_list/', views.post_list, name='posts_list'),
]
