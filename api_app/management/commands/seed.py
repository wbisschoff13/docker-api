
from django.core.management.base import BaseCommand
from ...views import get_pokemon
import aiohttp
import asyncio
from asgiref.sync import async_to_sync


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_pokemon()
