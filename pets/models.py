from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)

    def get_registrations(self):
        return self.petregistration_set.all()

    def is_registered(self):
        return self.get_registrations().count() > 0

    def __str__(self):
        return '{}'.format(self.name)


class PetRegistration(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} registered on {}'.format(self.pet.name, self.created_at)
