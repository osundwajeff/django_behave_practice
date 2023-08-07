from django import forms
from .models import PointOfInterest, PointOfInterestType, PointOfInterestCondition


class PointOfInterestForm(forms.ModelForm):
    class Meta:
        model = PointOfInterest
        fields = '__all__'


class PointOfInterestConditionForm(forms.ModelForm):
    class Meta:
        model = PointOfInterestCondition
        exclude = ('data',)

