from pyexpat import model
from rest_framework import serializers
# becouse we are serializing Pokemon from models file:
from .models import Pokemon 




class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        field = '__all__' # if we want to choose fields, user  field =['name', 'type']
                          # if we want all except => exlude  =['name', 'type']