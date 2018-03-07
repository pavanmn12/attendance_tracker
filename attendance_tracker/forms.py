
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Attendance


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.')
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.')
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class CheckinnForm(forms.Form):
    date = forms.DateField(label='date')
    checkinn = forms.TimeField(label='checkinn')


class CheckoutForm(forms.Form):
    date = forms.DateField(label='date')
    checkout = forms.TimeField(label='checkout')


class DashboardForm(forms.Form):
    fdate = forms.DateField(label='fdate')
    tdate = forms.DateField(label='tdate')
