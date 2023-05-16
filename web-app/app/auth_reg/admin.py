from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Longitude)
admin.site.register(Latitude)
admin.site.register(City)
admin.site.register(Device)
admin.site.register(Measurements)

