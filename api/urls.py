from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListKeyGen.as_view()),
]
