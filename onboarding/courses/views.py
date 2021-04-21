from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.publish.all()
    return render(request, 'courses/course/list.html', {
        'courses': courses
    })


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course/detail.html', {
        'course': course
    })

