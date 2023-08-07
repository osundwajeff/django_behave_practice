from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PointOfInterestForm, PointOfInterestConditionForm
from .models import PointOfInterest, PointOfInterestType, PointOfInterestCondition, Condition

# Create your views here.
# views.py


def home(request):
    return render(request, 'index.html')


def point_of_interest(request):
    point_of_interest_records = PointOfInterest.objects.all()
    return render(request, 'point_of_interest.html', {'records': point_of_interest_records})


def point_of_interest_type(request):
    point_of_interest_type_records = PointOfInterestType.objects.all()
    return render(request, 'point_of_interest_type.html', {'records': point_of_interest_type_records})


def point_of_interest_condition(request):
    point_of_interest_condition_records = PointOfInterestCondition.objects.all()
    return render(request, 'point_of_interest_condition.html', {'records': point_of_interest_condition_records})


def condition(request):
    condition_records = Condition.objects.all()
    return render(request, 'condition.html', {'records': condition_records})


def page_404(request, response):
    return HttpResponse('404 - Page Not Found', status=404)


def create_point_of_interest(request):
    if request.method == 'POST':
        form = PointOfInterestForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('point_of_interest')
        else:
            print(form.errors)
    else:
        form = PointOfInterestForm()

    point_of_interest_records = PointOfInterest.objects.all()
    point_of_interest_types = PointOfInterestType.objects.all()

    return render(request, 'point_of_interest.html', {
        'form': form,
        'point_of_interest_types': point_of_interest_types,
        'records': point_of_interest_records,
    })


def create_point_of_interest_condition(request):
    if request.method == 'POST':
        form = PointOfInterestConditionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new PointOfInterestCondition object
            form.save()
            # Redirect to the page where the list of PointOfInterestConditions is displayed
            return redirect('point_of_interest_condition')
        else:
            print(form.errors)
    else:
        form = PointOfInterestConditionForm()

    point_of_interest_records = PointOfInterest.objects.all()
    condition_records = Condition.objects.all()

    return render(request, 'create_point_of_interest_condition.html',{
        'form': form,
        'condition': condition_records,
        'point_of_interest': point_of_interest_records, })
