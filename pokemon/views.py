
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Pokemon
from .serializers import ListSerializer
def get_pokemon(request, pokemon_id):
    return HttpResponse(Pokemon.objects.get(id =pokemon_id))


def get_pokemons_list(request):
    poks = Pokemon.objects.all().values_list("name", flat = True)
    pok_list = "\n".join(f"<li>{pok}<li>" for pok in poks)
    return HttpResponse(f"<i>{pok_list}</i>")

class PokeListApiView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = ListSerializer
    """
    -we have to use queryset
    -CLASS.objects gives use alot of options. we can use all() or 
     get(id= pok_id)<< for example. 
     
     - to add filter    queryset = Pokemon.objects.all().filter(name = 'poke1')
    """