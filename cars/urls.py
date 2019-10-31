# cars/urls.py

from django.contrib import admin
from django.urls import path
from . import views
app_name = 'cars'
urlpatterns=[
    path('car_create/' , views.CreateCarView.as_view(),name='car_create'),
    path('car_list/' , views.CarListView.as_view(),name='car_list'),
    path('<int:pk>/' , views.CarDetailView.as_view(),name='car_detail'),
    path('<int:pk>/delete/',views.CarDeleteView.as_view(),name='car_delete'),
    path('create_reservation/',views.CreateReservationView.as_view(),name='create_reservation'),
    path('reservation_list/' ,views.ReservationListView.as_view() ,name='reservation_list'),
    path('reservation_detail/<int:pk>/',views.ReservationDetailView.as_view(),name='reservation_detail'),

]
