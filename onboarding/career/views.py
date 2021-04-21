from django.shortcuts import render


def career(request):
    return render(request, 'career/mentor.html')