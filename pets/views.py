from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from pets import models as pet_models


@login_required
@csrf_exempt
def register_pet(request):
    if request.method == "POST":
        pet_id = request.POST.get('pet_id')
        pet = pet_models.Pet.objects.get(pk=pet_id)
        if pet.is_registered():
            status_code = 400
            message = "Already registered"
        else:
            pet_models.PetRegistration.objects.create(pet=pet)
            status_code = 201
            message = "Registered pet"
    else:
        status_code = 405
        message = "Method not allowed"
    return HttpResponse(content=message, status=status_code)
