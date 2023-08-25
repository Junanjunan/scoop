from django.urls import path

from . import views

urlpatterns = [
    path("first-user", views.first_user_view),
]
