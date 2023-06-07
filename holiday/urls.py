from django.urls import path
from holiday import views


urlpatterns = [
    path('holiday/', views.HolidayList.as_view()),
    path('holiday/<int:pk>', views.HolidayDetail.as_view()),
]
