from django.contrib import admin

from pets import models


admin.site.register(models.Pet)
admin.site.register(models.PetRegistration)
