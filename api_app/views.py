from .models import Pokemon
from .serializers import PokemonSerializer, PokemonDetailSerializer, StatSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Avg, F, IntegerField, Sum


class PokemonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PokemonDetailSerializer
        return PokemonSerializer


class StatViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset().order_by(-average_stat())
        if 'type' in self.kwargs:
            queryset = queryset.filter(type1=self.kwargs['type'])
        serializer = self.get_serializer(queryset, many=True)

        aggregate_avg = (queryset.annotate(
            stats=average_stat()).aggregate(Avg('stats')))

        response_data = {'average_stats': round(aggregate_avg['stats__avg']),
                         'result': serializer.data}

        return Response(response_data)


def average_stat():
    return (F('hp') + F('attack') + F('defense') +
            F('sp_attack') + F('sp_defense') + F('speed')) / 6
