from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/portfolio.html")

def about(request):  # New view for About Me page
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def projects(request):
    return render(request, "pages/projects.html")
