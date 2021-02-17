from django.test import TestCase
from api_app.models import Pokemon
from rest_framework.test import APIClient, APIRequestFactory
# Create your tests here.


class PokemonTestCase(TestCase):
    def setUp(self):
        Pokemon.objects.create(id=1, name="charmander", type1="fire")
        Pokemon.objects.create(id=2, name="bulbasaur", type1="grass", hp="10", attack="10",
                               defense="10", sp_attack="10", sp_defense="10", speed="10")

    def test_average_stat(self):
        charmander = Pokemon.objects.get(name="charmander")
        bulbasaur = Pokemon.objects.get(name="bulbasaur")
        self.assertEqual(charmander.average_stat, 0)
        self.assertEqual(bulbasaur.average_stat, 10)

    def test_api(self):
        client = APIClient()
        response = client.get('/pokemon/')
        self.assertEqual(response.status_code, 200)
