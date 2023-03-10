from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Model
from .forms import MyModelForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def laboratory_six(request):
    model_db = Model.objects.all()
    return render(request, 'main/laboratory_six.html', {'model_db': model_db})


def add_record(request):
    error = ''
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab6')
        else:
            error = 'Ошибка добавления записи'

    form = MyModelForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_records.html', data)


def laboratory_seven(request):
    return render(request, 'main/laboratory_seven.html')


def laboratory_eight(request):
    return render(request, 'main/laboratory_eight.html')


def laboratory_nine(request):
    return render(request, 'main/laboratory_nine.html')
