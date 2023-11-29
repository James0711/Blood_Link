from django.contrib import admin
from .models import Otp, Appointment

# Register your models here.
admin.site.site_header = "Blood_Link Admin"
admin.site.site_title = "Blood_Link Admin Portal"
admin.site.index_title = "Welcome to Blood_Link Admin Portal"
admin.site.register(Otp)
admin.site.register(Appointment)
