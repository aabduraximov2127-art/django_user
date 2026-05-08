from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_view, name="user_view"),
    path("create/", views.user_create, name="user_create"),
    path("delete/<int:id>/", views.user_delete, name="user_delete"),
    path("update/<slug:slug>/", views.user_update, name="user_update"),
    path("detail/<slug:slug>/", views.user_detail, name="user_detail"),
]