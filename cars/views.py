from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView,UpdateView,
                                ListView,
                                  DetailView)
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.views.generic.edit import DeleteView
from django.urls import reverse ,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
# Create your views here.

class CreateCarView(CreateView):
    # login mixin requiries
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    template_name = 'cars/car_create.html'
    model = models.CarModel
    fields = ['title', 'year_model', 'autogeartype', 'doors',
              'seats', 'base_price', 'description', 'image']
    #
    def get_form(self, form_class=None):
        return forms.CarModelForm

    def post(self ,request , *args , **kwargs):
        print(request)
        form = forms.CarModelForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return HttpResponseRedirect(reverse('cars:car_detail',kwargs={'pk':object.pk}))
        else :
            print(form.errors)
        return render(request , self.template_name , {'form' : form})


class CarListView(ListView):
    model = models.CarModel
    template_name = 'cars/car_list.html'

class CarDetailView(DetailView):
    model = models.CarModel
    template_name = 'cars/car_detail.html'

class CarDeleteView(DeleteView):
    # model = models.CarModel
    model = models.CarModel
    template_name = 'cars/delete_view.html'
    success_url = reverse_lazy('cars:car_list')
    # DeleteView.model = model
    # DeleteView.template_name= 'cars/delete_view.html'
    # DeleteView.success_url = reverse_lazy('cars:car_list')
    # def get_object(self , queryset=None):
    #     pk = self.kwargs.get('pk')
    #     return get_object_or_404(self.model , pk)


class CreateReservationView(CreateView):
    # login mixin requiries
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'cars/create_reservation.html'
    model = models.ReservationModel
    def get_form(self, form_class=None):
        return forms.ReservationModelForm

    def post(self, request, *args, **kwargs):
        form = forms.ReservationModelForm(request.POST)

        if form.is_valid():

            object = form.save(commit=False)

            ## because it is a foreign key we had to get user instance first
            user = User.objects.get(username=request.user)

            object.reserver = user
            object.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
        return render(request , self.template_name , {'form' : form})


class ReservationListView(ListView):
    model = models.ReservationModel
    template_name = 'cars/reservation_list.html'

class ReservationDetailView(DetailView):
    model = models.ReservationModel
    template_name = 'cars/reservation_detail.html'

