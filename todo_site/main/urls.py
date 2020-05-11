from django.urls import path
from . import views 
from django.http import HttpResponse

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view")

]