from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("create/", views.user_create, name="user_create"),
    path("update/<slug:slug>/", views.user_update, name="user_update"),
    path("delete/<int:id>/", views.user_delete, name="user_delete"),
    path('user/<slug:slug>/', views.user_detail, name='user_detail'),
    path("register/", views.register_view, name="register_view"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('users/', views.user_list, name='user_list'),
]