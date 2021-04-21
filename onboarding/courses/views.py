from django.shortcuts import render, get_object_or_404
from .models import *


def course_list(request):
    courses = Course.published.all()
    return render(request, 'courses/course/list.html', {
        'courses': courses
    })


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if course.type == 'game':
        content = Game.objects.get(course=course)
    elif course.type == 'doc':
        content = Document.objects.get(course=course)
    elif course.type == 'test':
        content = Test.objects.get(course=course)

    return render(request, 'courses/course/detail.html', {
        'course': course,
        'content': content,
    })

