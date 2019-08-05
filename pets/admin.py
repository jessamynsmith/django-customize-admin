from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from pets import models


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'register_or_deregister']

    def register_or_deregister(self, obj):
        if obj.is_registered():
            registration_date = obj.get_registrations()[0].created_at
            display_text = 'Pet registered on {}'.format(registration_date)
        else:
            display_text = format_html('<a href="#" class="register" data-pet_id="{}"'
                                       'data-register_url="{}">Register</a>'.format(
                                        obj.pk, reverse('register_pet')))
        return display_text

    class Media:
        js = ("pets/register_pet.js",)


class PetRegistrationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.PetRegistration, PetRegistrationAdmin)
