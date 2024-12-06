from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def xxx(request, y):
    lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return render(
        request,
        "xxx.html",
        {"klucz": y, "lista": lista}
    )


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        "post_list.html",
        {"posts": posts}
    )

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "post_details.html",
        {"post": post}
    )   