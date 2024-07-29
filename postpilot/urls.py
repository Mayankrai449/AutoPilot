from django.urls import path
from .views import schedule_post, dashboard

urlpatterns = [
    path('schedule/', schedule_post, name='schedule_post'),
    path('dashboard/', dashboard, name='dashboard'),
]
