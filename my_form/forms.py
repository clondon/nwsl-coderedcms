# https://www.youtube.com/watch?v=VOddmV4Xl1g 
from django.forms import ModelForm
from .models import Customer

class CustomerForm(modelForm):
    class Meta:
        """ Customer form model """
        model = Customer
        field = '__all__'

