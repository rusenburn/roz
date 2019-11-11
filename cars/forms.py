from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import CarModel , CarCommercialModel,ReservationModel


class CarModelForm(ModelForm):

    class Meta:
        model = CarModel
        fields = ('title' , 'year_model' , 'autogeartype' , 'doors',
                    'seats' , 'base_price' , 'description' , 'image')
        labels = {
            'title': _("Title"),
            'year_model': _('Year Model'),
            'autogeartype' : _('Automatic Gear ?'),
            'doors' : _('Number of Doors'),
            'seats' : _('Number of Seats'),
            'base_price': _('Base Price'),
            'description' : _('Description'),
            'image' : _('Image'),

        }
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control',
                                             'placeholder' : 'Enter Title'}),
            'year_model' : forms.NumberInput(attrs={'class' : 'form-control',
                                                    'placeholder' : '2019'}),
            'autogeartype':forms.CheckboxInput(),
            'doors':forms.NumberInput(),
            'seats':forms.NumberInput(),
            'base_price' : forms.NumberInput(),
            'description' : forms.TextInput(attrs={'class':'form-control'}),

        }



        help_texts = {
            'title': _('Some useful help text.'),
        }


class CarCommercialModelForm(ModelForm):
    class Meta:
        model = CarCommercialModel
        fields= ('en_title' , 'ar_title' , 'featured' , 'car' , 'days' , 'price')

        labels={
            'en_title' : 'English Title' ,
            'ar_title' : _('Arabic Title'),
            'featured' : _('Featured'),
            'car' : _('Car'),
            'days' : _('Number of days'),
            'price' : _('Price')
        }

class ReservationModelForm(ModelForm):

    class Meta:

        model = ReservationModel
        fields = ('number_of_days', 'offer' ,'first_name' , 'last_name'
                  , 'age', 'location' , 'start_date')
        labels={
            'reserver' : _('Reserver Account'),
            'offer' : _('Choose Offer'),
            'first_name' : _('First Name') ,
            'last_name' : _('Last Name'),
            'age' : _('Age'),
            'start_date' : _('Reservation Date'),
            'number_of_days' : _('Reservation Days'),
            'location' : _('Delivery Location'),

        }

        widgets ={
            'reserver' : forms.HiddenInput(attrs={'required' : 'false'}),
            'start_date' : forms.SelectDateWidget(),
            'number_of_days' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.NumberInput(attrs={'class' : 'form-control'}) ,



        }

    def clean_reserver(self):
        reserver = self.cleaned_data['reserver']
        return reserver
