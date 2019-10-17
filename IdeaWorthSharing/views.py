from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'IdeaWorthSharing/home.html', {})

def tweet(request):
    return render(request, 'IdeaWorthSharing/tweet.html', {})

def trial(request):
    return render(request, 'IdeaWorthSharing/trial.html', {})
