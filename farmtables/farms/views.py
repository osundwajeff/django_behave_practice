from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import UpdateView

from .forms import PointOfInterestForm, PointOfInterestConditionForm
from .models import PointOfInterest, PointOfInterestType, PointOfInterestCondition, Condition


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class PointOfInterestView(View):
    def get(self, request):
        point_of_interest_records = PointOfInterest.objects.all()
        return render(request, 'point_of_interest.html', {'records': point_of_interest_records})


class PointOfInterestTypeView(View):
    def get(self, request):
        point_of_interest_type_records = PointOfInterestType.objects.all()
        return render(request, 'point_of_interest_type.html', {'records': point_of_interest_type_records})


class PointOfInterestConditionView(View):
    def get(self, request):
        point_of_interest_condition_records = PointOfInterestCondition.objects.all()
        condition_records = Condition.objects.all()
        poi_records = PointOfInterest.objects.all()
        return render(request, 'point_of_interest_condition.html', {
            'records': point_of_interest_condition_records,
            'condition_records': condition_records,
            'poi_records': poi_records
        })


class ConditionView(View):
    def get(self, request):
        condition_records = Condition.objects.all()
        return render(request, 'condition.html', {'records': condition_records})


class Page404View(View):
    def get(self):
        return HttpResponse('404 - Page Not Found', status=404)


class CreatePointOfInterestView(View):
    def get(self, request):
        form = PointOfInterestForm()
        point_of_interest_records = PointOfInterest.objects.all()
        point_of_interest_types = PointOfInterestType.objects.all()
        return render(self.request, 'point_of_interest.html', {
            'form': form,
            'point_of_interest_types': point_of_interest_types,
            'records': point_of_interest_records,
        })

    def post(self, request):
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_point_of_interest')
        else:
            print(form.errors)
            return redirect('create_point_of_interest')


class CreatePointOfInterestConditionView(View):

    def get(self, request):
        form = PointOfInterestConditionForm()
        point_of_interest_records = PointOfInterest.objects.all()
        condition_records = Condition.objects.all()
        return render(request, 'create_point_of_interest_condition.html', {
            'form': form,
            'condition': condition_records,
            'point_of_interest': point_of_interest_records,
        })

    def post(self, request):
        form = PointOfInterestConditionForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect('point_of_interest_condition')
        else:
            print(form.errors)
            return redirect('point_of_interest_condition')


class DeletePointOfInterestView(View):
    def post(self, request):
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        try:
            # Retrieve the PointOfInterest record to delete
            poi_to_delete = PointOfInterest.objects.get(latitude=latitude, longitude=longitude)

            # Delete the record from the database
            poi_to_delete.delete()

            return JsonResponse({"message": "Point of interest deleted successfully"})
        except PointOfInterest.DoesNotExist:
            return JsonResponse({"error": "Point of interest not found"}, status=404)

    def http_method_not_allowed(self, request):
        return JsonResponse({"error": "Invalid request method"})


class PointOfInterestConditionUpdateView(UpdateView):
    model = PointOfInterestCondition
    fields = ['condition', 'date', 'notes', 'image']  # List of fields to be updated
    template_name = 'point_of_interest_condition.html'
    success_url = reverse_lazy('condition')  # URL to redirect after successful update

    def form_valid(self, form):
        # Additional logic if needed before saving the form
        return super().form_valid(form)