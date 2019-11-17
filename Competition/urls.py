from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTracks.as_view()),
    path('<int:pk>/', views.DetailTrack.as_view()),
]