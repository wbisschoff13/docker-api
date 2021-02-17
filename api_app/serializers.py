from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['url', 'id', 'name', 'type1', 'type2', 'average_stat']


class PokemonDetailSerializer(serializers.ModelSerializer):
    average_stat = serializers.IntegerField()

    class Meta:
        model = Pokemon
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ['id', 'name']
