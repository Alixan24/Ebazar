from django.shortcuts import render # type: ignore

def home(request):
    return render(request, "main/homepage.html")
# Create your views here.
