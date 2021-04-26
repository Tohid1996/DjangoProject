from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# from django.views.generic import FormView

from post.models import Post


# class ShowView(FormView):
#     template_name = 'post_list.html'


def index(request):
    return HttpResponse("Welcome to post")


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now())
    return render(request, 'post_list.html', {'posts': posts})
