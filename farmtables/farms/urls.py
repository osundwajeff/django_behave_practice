from django.urls import path
from .views import (
    HomeView,
    PointOfInterestView,
    CreatePointOfInterestView,
    PointOfInterestTypeView,
    PointOfInterestConditionView,
    ConditionView,
    CreatePointOfInterestConditionView,
    Page404View, DeletePointOfInterestView, PointOfInterestConditionUpdateView,
)

urlpatterns = [
    path("",
         HomeView.as_view(),
         name="index"),  # Default URL pattern for the root path
    path("home/",
         HomeView.as_view(),
         name="index"),
    path("point_of_interest/",
         PointOfInterestView.as_view(),
         name="point_of_interest"),
    path("create_point_of_interest/",
         CreatePointOfInterestView.as_view(),
         name="create_point_of_interest"),
    path("point_of_interest_type/",
         PointOfInterestTypeView.as_view(),
         name="point_of_interest_type"),
    path("point_of_interest_condition/",
         PointOfInterestConditionView.as_view(),
         name="point_of_interest_condition"),
    path("condition/",
         ConditionView.as_view(),
         name="condition"),
    path(
        "create_point_of_interest_condition/",
        CreatePointOfInterestConditionView.as_view(),
        name="create_point_of_interest_condition"),
    path("404/",
         Page404View.as_view(),
         name="404"),
    path('delete_point_of_interest/',
         DeletePointOfInterestView.as_view(),
         name='delete_point_of_interest'),
    path('update/<int:pk>/',
         PointOfInterestConditionUpdateView.as_view(),
         name='update_point_of_interest_condition'),
]