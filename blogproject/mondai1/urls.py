from django.urls import path
from . import views

app_mane = 'mondai1'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('question/', views.QuestionView.as_view(), name='question'),
]