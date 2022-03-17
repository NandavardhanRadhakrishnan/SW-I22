from django.contrib import admin

# Register your models here.

# register job_seeker model
from .models import Job_seeker
admin.site.register(Job_seeker)