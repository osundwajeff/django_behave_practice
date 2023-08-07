from django.shortcuts import render
from django.http import Http404
from .models import PointOfInterest, PointOfInterestType
from .models import PointOfInterestCondition

# Create your views here.
# views.py
def home(request):
    return render(request, 'farm/home.html')


def point_of_interest(request):
    point_of_interest_records = PointOfInterest.objects.all()
    return render(request, 'farm/point_of_interest.html', {'records': point_of_interest_records})


def point_of_interest_type(request):
    point_of_interest_type_records = PointOfInterestType.objects.all()
    return render(request, 'farm/point_of_interest_type.html', {'records': point_of_interest_type_records})


def point_of_interest_condition(request):
    point_of_interest_condition_records = PointOfInterestCondition.objects.all()
    return render(request, 'farm/point_of_interest_condition.html', {'records': point_of_interest_condition_records})


def page_404(request, exception):
    return render(request, 'farm/404.html', status=404)
