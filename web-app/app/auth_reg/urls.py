from django.urls import path, include
from .views import register_view, login_view, user_logout, edit_profile, profile

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name='profile'),
]