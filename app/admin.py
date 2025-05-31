from django.contrib import admin
from .models import Menu, Reservation, Category

# Register your models here.


admin.site.register(Menu)
admin.site.register(Reservation)
admin.site.register(Category)