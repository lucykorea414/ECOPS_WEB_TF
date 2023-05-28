from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = "users"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register/", views.register, name='register'),
    # path('profile/<int:pk>', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
    path('profile_edit/<int:pk>', login_required(views.EditProfileView.as_view()), name='profile_edit'),
    # path('add_comment', views.add_comment, name='add_comment'),
    path('profile/<int:pk>/add_comment', views.add_comment_view, name='add_comment'),
]