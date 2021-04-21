from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:slug>/', views.course_detail, name='course_detail')
]