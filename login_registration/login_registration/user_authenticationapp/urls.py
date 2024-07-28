from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.home,name="home"),
    path("register/",views.registration,name="register"),
    path("login/",views.loginpage,name="login"),
    path("logout/",views.logoutpage,name="logout")
]