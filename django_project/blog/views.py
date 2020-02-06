# shortcut to import the rendering of the html file for the httprequest allows to render the template
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.
# handles traffic from home page


# dummy data
# posts = [
#     {
#         'author': 'Me shock',
#         'title': 'first post',
#         'content': 'First post content',
#         'date_posted': 'March, 22 1999'
#     },
#     {
#         'author': 'Me shock',
#         'title': 'second post',
#         'content': 'second post content',
#         'date_posted': 'May, 5 2019'
#     },

# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')

    # has 3 possible arguments
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1> Blog about</h1>')
    # has 3 possible arguments
    return render(request, 'blog/about.html', {'title': 'About'})
