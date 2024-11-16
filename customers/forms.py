from django import forms
from customers.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'admissionNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Admission Number'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Telephone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'gender': forms.RadioSelect(choices=Customer.GENDER_CHOICES),
            'county': forms.Select(choices=Customer.KENYA_COUNTIES),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'images/*'}),
        }
