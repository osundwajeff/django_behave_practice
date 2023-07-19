from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import PointOfInterest, PointOfInterestType
from .models import PointOfInterestCondition, Condition

# Register your models here.
@admin.register(PointOfInterest)
class PointOfInterestAdmin(OSMGeoAdmin):
    list_display = (
        "notes", "image", "height_m", "installation_date", "is_date_estimated")
    search_fields = ["notes"]
    list_filter = ["point_of_interest_type"]


@admin.register(PointOfInterestType)
class PointOfInterestTypeAdmin(OSMGeoAdmin):
    list_display = ("name", "notes", "image")
    search_fields = ["name", "notes"]


@admin.register(PointOfInterestCondition)
class PointOfInterestConditionAdmin(OSMGeoAdmin):
    list_display = ("notes", "image")
    search_fields = ["notes"]
    list_filter = ["point_of_interest", "condition"]


@admin.register(Condition)
class ConditionAdmin(OSMGeoAdmin):
    list_display = ("notes", "image")
    search_fields = ["notes"]