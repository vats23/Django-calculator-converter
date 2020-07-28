from django.urls import path,include
from . import views

app_name = "wallet"

urlpatterns = [
    path("about/",views.about,name="about"),
    path("login/",views.user_login,name="user_login"),
    path("logout/",views.user_logout,name="user_logout"),
    path("register/",views.register,name="register"),
    path("dashboard/",views.dashboard,name="dashboard")
]
