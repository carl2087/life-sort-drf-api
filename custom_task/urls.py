from django.urls import path
from custom_task import views

urlpatterns = [
    path('customtask/', views.CustomTaskList.as_view()),
]
