from django.http import HttpResponse

from .models import Pokemon
def get_pokemon(request, pokemon_id):
    return HttpResponse(Pokemon.objects.get(id =pokemon_id))