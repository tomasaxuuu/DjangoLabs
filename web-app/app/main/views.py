from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from .models import Model
from .forms import MyModelForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def laboratory_six(request):
    attribute_to_sort = request.GET.get('sort')
    if attribute_to_sort:
        model_db = Model.objects.all().order_by(attribute_to_sort)
    else:
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


def delete_record(request, el_id):
    event = Model.objects.get(pk=el_id)
    event.delete()
    return redirect('lab6')


class UpdateRecord1(UpdateView):
    model = Model
    template_name = 'main/edit.html'
    fields = ['id', 'latitude', 'longitude', 'temperature', 'data_and_time']


def laboratory_eight(request):
    return render(request, 'main/laboratory_eight.html')


def laboratory_nine(request):
    return render(request, 'main/laboratory_nine.html')
