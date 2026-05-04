from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blogpost, Comment


# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    return render(request, "blog/index.html", {"myposts": myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id).first()

    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")

        Comment.objects.create(
            post=post, name=name, comment=comment
        )

        return redirect("BlogPost", id=post.post_id)

    return render(request, "blog/blogpost.html", {"post": post, "comments": comments})
