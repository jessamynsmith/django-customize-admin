from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)


class PetRegistration(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} registered on {}'.format(self.pet.name, self.created_at)
