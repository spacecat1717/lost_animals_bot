import asyncio
import httpx

from config.config import MAP_TOKEN
from config.log_config import Logger as Log


class Geocoder:

    async def get_location_data(self, location: str) -> tuple:
        Log.logger.info('[GEOCODER]Making request to API')
        url = f'https://geocode-maps.yandex.ru/1.x?format=json&lang=ru_RU&kind=district&geocode={location}&apikey={MAP_TOKEN}'
        async with httpx.AsyncClient(trust_env=True) as client:
            response = await client.get(url)
        if response.status_code == 200:
            city = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][4]["name"]
            district = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
            Log.logger.info('[GEOCODER] Location data has been found')
            return city, district
        Log.logger.error("[GEOCODER] API returned code %r, data hasn't been found", response.status_code)



