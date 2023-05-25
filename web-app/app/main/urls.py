from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('laboratory_six', views.laboratory_six, name='lab6'),
    path('laboratory_eight', views.laboratory_eight, name='lab8'),
    path('laboratory_nine', views.laboratory_nine, name='lab9'),
    path('add_record', views.add_record, name='add_record'),
    path('delete/<int:el_id>', views.delete_record, name='delete_record'),
    path('update/<int:pk>', views.UpdateRecord1.as_view(), name='update_record1'),
]
