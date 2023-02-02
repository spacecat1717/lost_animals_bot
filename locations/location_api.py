import asyncio
import httpx

from config.config import MAP_TOKEN
from config.log_config import Logger as Log
from database.connection import Connection

class Geocoder:
    def __init__(self):
        self._connection = Connection()

    async def smth(self, location: str):
        get_city_url = f'https://geocode-maps.yandex.ru/1.x?format=json&lang=ru_RU&kind=district&geocode={location}&apikey={MAP_TOKEN}'
        async with httpx.AsyncClient(trust_env=True) as client:
            response_city = await client.get(get_city_url)
        print(response_city.json())


g = Geocoder()
asyncio.run(g.smth('59.918085,30.349826'))


