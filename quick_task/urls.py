from django.urls import path
from quick_task import views

urlpatterns = [
    path('quicktask/', views.QuickTaskList.as_view()),
]
