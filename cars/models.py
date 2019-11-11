from django.db import models
from django.urls import reverse
from accounts.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class CarModel(models.Model):
    title = models.CharField(max_length=256 , unique=True )
    year_model = models.IntegerField()
    autogeartype = models.BooleanField(default=True)
    doors = models.SmallIntegerField(default=4)
    seats = models.SmallIntegerField()
    base_price = models.PositiveIntegerField(default=1 ,blank=True)
    description = models.TextField(blank=True,max_length=500)
    image = models.ImageField(blank=True , upload_to='car_profile')

    class Meta:
        default_permissions= ('change' , 'add' , 'delete' , 'view')

    def get_absolute_url(self) :
        return reverse('cars:car_detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.title

class CarCommercialModel(models.Model):
    en_title = models.CharField(max_length=128)
    ar_title = models.CharField(max_length=128)
    featured = models.BooleanField()
    car = models.ForeignKey(CarModel,on_delete='CASCADE',related_name='commercials')
    days = models.SmallIntegerField(default=3)
    price = models.DecimalField(max_digits=6,decimal_places=2 ,default=29.99)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.en_title

    def get_absolute_url(self):
        return reverse('cars:commercial_detail',kwargs={'pk' : self.pk})

    def go_featured(self):
        self.featured = True
        self.save()
        print(self.featured)

    def go_unfeatured(self):
        print(self.featured)
        self.featured = False
        self.save()
        print(self.featured)


class ReservationModel(models.Model):
    reserver = models.ForeignKey(get_user_model(),on_delete='CASCADE',related_name='reservations')
    offer = models.ForeignKey(CarModel ,on_delete='CASCADE', related_name='reservervations')
    ordered_date = models.DateTimeField (auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=10 , blank=True)
    last_name = models.CharField(max_length=10 , blank=True)
    age = models.IntegerField(blank=True)
    start_date = models.DateTimeField()
    number_of_days = models.IntegerField(default=1)
    location = models.CharField(max_length=256,choices=[('Amman' , 'Amman'),
                                         ('Aqaba' , 'Aqaba'),
                                         ('Irbid' , 'Irbid'),
                                         ])
