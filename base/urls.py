from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("todo/", views.homepage, name="home"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("delete-task/<str:pk>/", views.delete_task, name="delete-task"),
    path("update_user/<str:pk>/", views.update_user, name="update-user"),
]