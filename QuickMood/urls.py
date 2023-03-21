from django.urls import path

from QuickMood import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage')
]
