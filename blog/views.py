from django.shortcuts import render
from .models import Post


def post_list(request):
    p_list = Post.objects.all()
    data = {
        'p_list': p_list
    }
    return render(request, 'blog/post_list.html', context=data)
