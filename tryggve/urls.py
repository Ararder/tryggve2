from django.urls import path
from tryggve import views

urlpatterns = [
    path("", views.home, name="home"),
]