from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home_page'),
    path('laboratory_six', views.laboratory_six, name='lab6'),
    path('laboratory_seven', views.laboratory_seven, name='lab7'),
    path('laboratory_eight', views.laboratory_eight, name='lab8'),
    path('laboratory_nine', views.laboratory_nine, name='lab9'),
    path('add_record', views.add_record, name='add_record'),
]
