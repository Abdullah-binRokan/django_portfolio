from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def blog_view(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {"posts": posts})


def add_post_view(request: HttpRequest):
    # using django ModelForm
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, "Post added successfuly!")
        else:
            messages.error(request, "There was an error. Please try again.")
    else:
        post_form = PostForm()

    return render(request, "blog/add_post.html")


def update_post_view(request: HttpRequest, post_id: int):
    try:
        # get the post by the id
        post = Post.objects.get(pk = post_id)

        # Check if the form was submited by post method
        if request.method == "POST":
            post.name = request.POST["name"]
            post.description = request.POST["description"]
            # check if the images updatedd
            if "image" in request.FILES:
                post.image = request.FILES["image"]
            if "details_image" in request.FILES:
                post.details_image = request.FILES["details_image"]
            post.save()
            messages.success(request, "post updated successfuly!")

    except:
        messages.error(request, "There was an error. Please try again.")

    return render(request, "blog/update_post.html", {"post": post})


def delete_post_view(request: HttpRequest, post_id):
    try:
        post = Post.objects.get(pk = post_id)
        post.delete()

    except:
        return redirect("dashboard:dashboard_posts_view")

    return render(request, "dashboard/posts.html")