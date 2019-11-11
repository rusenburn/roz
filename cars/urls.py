# cars/urls.py
from django.contrib.auth.decorators import permission_required
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'cars'
urlpatterns=[
    path('car_create/' , views.CreateCarView.as_view(),name='car_create'),
    path('car_list/' , views.CarListView.as_view(),name='car_list'),
    path('<int:pk>/' , views.CarDetailView.as_view(),name='car_detail'),
    path('<int:pk>/delete/',views.CarDeleteView.as_view(),name='car_delete'),
    path('<int:pk>/update/',views.UpdateCarView.as_view(),name='car_update'),
    path('commercial_create/' , views.CreateCarCommercialView.as_view(),name='commercial_create'),
    path('commercial_update/<int:pk>/',views.UpdateCarCommercialView.as_view(),name='commercial_update'),
    path('commercial_feature/<int:pk>/',permission_required('cars.update_carcommercialmodel')(views.UpdateCarCommercialView.go_featured_view),name='commercial_feature'),
    path('commercial_unfeature/<int:pk>/',permission_required('cars.update_carcommercialmodel')(views.UpdateCarCommercialView.go_unfeatured_view),name='commercial_unfeature'),
    path('commercial_list/',views.CarCommercialListView.as_view(),name='commercial_list'),
    path('commercial_detail/<int:pk>/',views.CarCommercialDetailView.as_view(),name='commercial_detail'),
    path('commercial_delete/<int:pk>/',views.CarCommercialDeleteView.as_view(),name='commercial_delete'),
    path('create_reservation/',views.CreateReservationView.as_view(),name='create_reservation'),
    path('reservation_list/' ,views.ReservationListView.as_view() ,name='reservation_list'),
    path('reservation_detail/<int:pk>/',views.ReservationDetailView.as_view(),name='reservation_detail'),

]
