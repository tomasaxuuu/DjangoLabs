from .models import Model
from django.forms import ModelForm, TextInput, DateTimeInput


class MyModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['latitude', 'longitude', 'temperature', 'data_and_time']

        widgets = {
            "latitude": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Введите широту'
            }),
            "longitude": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Введите долготу'
            }),
            "temperature": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Введите температуру'
            }),
            "data_and_time": DateTimeInput(attrs={
                'class': 'input',
                'placeholder': 'Дата'
            })
        }