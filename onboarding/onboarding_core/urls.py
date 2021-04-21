from django.urls import path
from . import views

app_name = 'onboarding_core'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('faq/', views.faq, name='faq'),
]