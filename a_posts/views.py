from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home_view(request):
    if request.method == "GET":
        print("Hello World")
    return render(request, "a_posts/home.html")
