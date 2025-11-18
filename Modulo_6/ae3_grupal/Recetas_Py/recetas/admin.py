from django.contrib import admin
from .models import Receta
from django.shortcuts import render, get_object_or_404

# Register your models here.
admin.site.register(Receta)
