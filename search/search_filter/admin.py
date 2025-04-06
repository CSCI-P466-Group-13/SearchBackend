from django.contrib import admin
from .models import property
from .models import car

# Register your models here.
admin.site.register(property)
admin.site.register(car)