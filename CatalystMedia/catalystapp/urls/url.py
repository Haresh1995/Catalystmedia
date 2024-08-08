from django.urls import path
from ..views.home_view import home_view
from ..views.login_view import MyloginView
from ..views.upload_view import upload_view

urlpatterns = [
    path("home/", home_view),
    path("login/", MyloginView.as_view()),
    path("upload/", upload_view),
]