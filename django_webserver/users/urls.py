from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("login/", ),
    path("logout/", ),
    path("register/", ),
]