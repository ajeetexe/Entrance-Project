from django.contrib import admin
from .models import *
from Entrance.forms import FormFillForms

# Register your models here.
class FormFillAdmin(admin.ModelAdmin):
    form = FormFillForms

    def save_model(self, request, obj, form, change):
        obj.user_name = request.username
        obj.save()

admin.site.register(FormFillModel,FormFillAdmin)
