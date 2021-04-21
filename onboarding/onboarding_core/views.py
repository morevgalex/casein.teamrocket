from django.shortcuts import render


def index(request):
    return render(request, 'onboarding_core/main.html')


def profile(request):
    return render(request, 'onboarding_core/profile.html')
