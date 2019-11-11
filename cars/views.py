from django.shortcuts import render,redirect , get_object_or_404
from django.views.generic import (CreateView,UpdateView,
                                ListView,
                                  DetailView)
from django.contrib.auth.mixins import PermissionRequiredMixin ,LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse ,reverse_lazy
from django.http import HttpResponseRedirect

from . import models
from . import forms

# Create your views here.

class CreateCarView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    permission_required = 'cars.create_carmodel'
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

        form = forms.CarModelForm(request.POST , request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return HttpResponseRedirect(reverse('cars:car_detail',kwargs={'pk':object.pk}))
        else :
            print(form.errors)
        return render(request , self.template_name , {'form' : form})

class UpdateCarView(PermissionRequiredMixin,UpdateView):
    permission_required = 'cars.change_carmodel'
    template_name = "cars/car_create.html"
    model = models.CarModel
    fields = ['title', 'year_model', 'autogeartype', 'doors',
              'seats', 'base_price', 'description', 'image']

    # def get_form(self, form_class=None):
    #     return forms.CarModelForm

    # def get(self, request, *args, **kwargs):
    #
    #     form = forms.CarModelForm(request.POST,request.FILES,instance=self.get_object())
    #     return render(request , self.template_name , {'form' : form})
    #
    # def post(self, request, *args, **kwargs):
    #
    #     form = forms.CarModelForm(request.POST,request.FILES,instance=self.get_object())
    #     if form.is_valid():
    #         object = form.save(commit=False)
    #         object.save()
    #         return HttpResponseRedirect(reverse('cars:car_detail',kwargs={'pk':object.pk}))
    #     else :
    #         print(form.errors)
    #     return render(request , self.template_name , {'form' : form})

class CarListView(ListView):
    model = models.CarModel
    template_name = 'cars/car_list.html'

class CarDetailView(DetailView):
    model = models.CarModel
    template_name = 'cars/car_detail.html'

#
# Assuming you have an application with an app_label foo and a model named Bar,
# to test for basic permissions you should use:
#
# add: user.has_perm('foo.add_bar')
# change: user.has_perm('foo.change_bar')
# delete: user.has_perm('foo.delete_bar')
# view: user.has_perm('foo.view_bar')



class CarDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'cars.delete_carmodel'
    # model = models.CarModel
    model = models.CarModel
    template_name = 'cars/delete_view.html'
    success_url = reverse_lazy('cars:car_list')


class CreateCarCommercialView(PermissionRequiredMixin,CreateView):
    permission_required = 'cars.create_carcommercialmodel'
    model = models.CarCommercialModel
    template_name = 'cars/create_carcommercialmodel.html'
    fields = ('en_title' , 'ar_title' , 'featured' , 'car' , 'days' , 'price')

    def get_form_class(self):
        return forms.CarCommercialModelForm
# reservations are currently deprecated

class UpdateCarCommercialView(PermissionRequiredMixin,UpdateView):
    permission_required = 'cars.update_carcommercialmodel'
    model = models.CarCommercialModel
    template_name = 'cars/create_carcommercialmodel.html'
    fields = ('en_title' , 'ar_title' , 'featured' , 'car' , 'days' , 'price')

    def get_form_class(self):
        return forms.CarCommercialModelForm

    def go_featured_view(request,pk):

        commercial = get_object_or_404(models.CarCommercialModel,pk=pk)
        commercial.go_featured()
        return redirect('cars:commercial_detail',pk=pk)

    def go_unfeatured_view(request,pk):
        commercial = get_object_or_404(models.CarCommercialModel,pk=pk)
        commercial.go_unfeatured()
        return redirect('cars:commercial_detail',pk=pk)

class CarCommercialDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'cars.delete_carcommercialmodel'
    model = models.CarCommercialModel
    template_name = 'cars/delete_view.html'
    success_url = reverse_lazy('cars:car_list')  ### to be updated

class CarCommercialListView(ListView):
    model = models.CarCommercialModel
    template_name = 'cars/carcommercialmodel_list.html'
    queryset = model.objects.order_by('-featured')

class CarCommercialDetailView(DetailView):
    model = models.CarCommercialModel
    template_name = 'cars/carcommercialmodel_detail.html'

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
