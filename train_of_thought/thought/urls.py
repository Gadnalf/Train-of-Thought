from django.urls import path
from thought import views

urlpatterns = [
    path('', views.thought, name='thought'),
]