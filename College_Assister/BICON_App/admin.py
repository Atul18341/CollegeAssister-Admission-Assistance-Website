from django.contrib import admin
from django.db import models
from .models import colleges,data_contributors
# Register your models here.
#models=[models.colleges,models.data_contributors]
admin.site.register(colleges)