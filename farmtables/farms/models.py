from django.contrib.gis.db import models

# Create your models here.


class PointOfInterestType(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='point_of_interest_types', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class PointOfInterest(models.Model):
    point_of_interest_type = models.ForeignKey(
        PointOfInterestType, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='point_of_interests',null=True, blank=True)
    height_m = models.FloatField(null=True)
    installation_date = models.DateField(null=True)
    is_date_estimated = models.BooleanField(default=False)
    #geometry = models.GeometryField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.notes}"


class Condition(models.Model):
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='conditions', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.notes}"


class PointOfInterestCondition(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    point_of_interest = models.ForeignKey(
        PointOfInterest, on_delete=models.CASCADE)
    condition = models.ForeignKey(
        Condition, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='point_of_interest_conditions', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.notes}"
