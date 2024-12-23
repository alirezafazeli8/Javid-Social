from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from django.forms import ModelForm
from django import forms


# Create your views here.
def home_view(request):

    all_posts = Post.objects.all()

    return render(request, "a_posts/home.html", {"all_posts": all_posts})


# post class form
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # set style to post form
        labels = {"title": "جاوید نام", "image": "جاوید عکس", "body": "جاوید متن"}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "یک متن جاوید بنویسید ...",
                    "class": "font1 ",
                }
            )
        }


# create post view
def create_post_view(request):
    # create instance of post model
    form = PostCreateForm()
    if request.method == "POST":
        # pass POST request to form
        form = PostCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")

    return render(request, "a_posts/create_post.html", {"post_create_form": form})
