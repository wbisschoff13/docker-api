from django.shortcuts import render
import requests
from .models import Pokemon

from asgiref.sync import async_to_sync, sync_to_async
import asyncio
from aiohttp import ClientSession
# Create your views here.


@sync_to_async
def save_pokemon(pokemon):
    pokemon.save()
    return pokemon


async def get_pokemon_details(entry, session):
    species_response = await session.request(method='GET', url=entry['url'])
    species_data = await species_response.json()
    try:
        evolves_from = species_data['evolves_from_species']['name']
    except:
        evolves_from = None
    pokemon_response = await session.request(method='GET', url=f"https://pokeapi.co/api/v2/pokemon/{species_data['id']}/")
    pokemon_data = await pokemon_response.json()

    try:
        type1 = pokemon_data['types'][0]['type']['name']
    except:
        type1 = "Normal"
    try:
        type2 = pokemon_data['types'][1]['type']['name']
    except:
        type2 = None
    try:
        hp = pokemon_data['stats'][0]['base_stat']
        attack = pokemon_data['stats'][1]['base_stat']
        defense = pokemon_data['stats'][2]['base_stat']
        sp_attack = pokemon_data['stats'][3]['base_stat']
        sp_defense = pokemon_data['stats'][4]['base_stat']
        speed = pokemon_data['stats'][5]['base_stat']
    except:
        hp = 0
        attack = 0
        defense = 0
        sp_attack = 0
        sp_defense = 0
        speed = 0

    name = entry['name']
    id = species_data['id']
    pokemon = Pokemon(id, name, type1, type2, evolves_from,
                      hp, attack, defense, sp_attack, sp_defense, speed)
    await save_pokemon(pokemon)


@async_to_sync
async def get_pokemon():
    async with ClientSession() as session:
        url = "https://pokeapi.co/api/v2/pokemon-species/?limit=1000"
        response = requests.get(url)
        raw = response.json()
        results = []
        results.extend(raw['results'])
        while raw['next'] != None:
            response = requests.get(raw['next'])
            raw = response.json()
            results.extend(raw['results'])
        await asyncio.gather(*[get_pokemon_details(entry, session) for entry in results])
