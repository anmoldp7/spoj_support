from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name = "home_view"),
    path("<str:pk>/delete_handle", views.delete_handle, name = "delete_handle"),
    path("<str:pk>/detailed_handle", views.detailed_view, name = "detailed_view")
]