from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),  # Default URL pattern for the root path
    path("home/", views.home, name="index"),
    path("point_of_interest/", views.point_of_interest, name="point_of_interest"),
    path("create_point_of_interest/", views.create_point_of_interest, name="create_point_of_interest"),
    path("point_of_interest_type/", views.point_of_interest_type, name="point_of_interest_type"),
    path("point_of_interest_condition/", views.point_of_interest_condition, name="point_of_interest_condition"),
    path("condition/", views.condition, name="condition"),
    path("create_point_of_interest_condition", views.create_point_of_interest_condition, name="create_point_of_interest_condition"),
    path("404/", views.page_404, name="404"),
]