from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('add/', views.student_detail),
]