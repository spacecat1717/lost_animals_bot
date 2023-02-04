"""This class can manage Ad objects"""

import asyncio

from datetime import date
from typing import List

from config.log_config import Logger as Log
from database.connection import Connection
from database.ads.ad import Ad


class AdManager:
    def __init__(self):
        self._connection = Connection()

    @staticmethod
    async def _create_ad_instance(type: str, owner_id: int, city: str, district: str, location: str, creation_date: date, photo1_path: str,
                                  photo2_path: str, photo3_path: str, name: str, species: str, description: str,
                                  chip: bool, ad_id: int, found=False, found_reason='') -> Ad:
        ad = Ad(type=type, owner_id=owner_id, city=city, district=district, location=location,
                creation_date=creation_date, photo1_path=photo1_path,
                photo2_path=photo2_path, photo3_path=photo3_path, name=name, species=species, description=description,
                chip=chip, ad_id=ad_id)
        return ad

    async def create_ad(self, type: str, owner_id: int, city: str, district: str, location: str, photo1_path: str,
                        photo2_path: str, photo3_path: str, name: str, species: str, description: str,
                        chip: bool) -> Ad or False:
        try:
            ad = await self._create_ad_instance(type=type, owner_id=owner_id, city=city, district=district, location=location,
                                                photo1_path=photo1_path, photo2_path=photo2_path, photo3_path=photo3_path,
                                                name=name, species=species, description=description, chip=chip,
                                                creation_date=date.today(), ad_id=0)
            await ad.save_ad()
            Log.logger.info('[DB] [AdManager] Record of ad %r has been created')
            return ad
        except Exception as e:
            Log.logger.error('[DB] [AdManager] Try to create record of ad %r failed. Reason: %r', e)
            return False

    async def get_user_ads(self, user_id: int) -> List[Ad]:
        command = (
            "SELECT * FROM ads WHERE owner=$1"
        )
        ads: List[Ad] = []
        async with self._connection as conn:
            res = await conn.fetch(command, user_id)
        print(res)
        for r in res:
            ad = await self._create_ad_instance(type=r[1], owner_id=user_id, location=r[3], creation_date=r[4],
                                                photo1_path=r[5], photo2_path=r[6], photo3_path=r[7], name=r[8],
                                                species=r[9], description=r[10], chip=r[11], found=r[12],
                                                found_reason=r[13], city=r[14], district=r[15], ad_id=r[0])
            ads.append(ad)
        Log.logger.info('[DB] [AdManager] Ads of user %r have been gotten', user_id)
        return ads

    async def get_with_filters(self, user_id: int, filters: list[dict]) -> List[Ad]:
        """Thing that can make sql request with custom filters
        IDK how to do it"""
        pattern = ''
        for f in filters[:-1]:
            pattern += f"{f['name']}='{f['value']}' AND "
        pattern += f"{filters[-1]['name']}='{filters[-1]['value']}'"
        command = (
            "SELECT * FROM ads WHERE {}"
        )
        sql = command.format(pattern)
        async with self._connection as conn:
            res = await conn.fetch(sql)
        ads: List[Ad] = []
        for r in res:
            ad = await self._create_ad_instance(type=r[1], owner_id=user_id, location=r[3], creation_date=r[4],
                                                photo1_path=r[5], photo2_path=r[6], photo3_path=r[7], name=r[8],
                                                species=r[9], description=r[10], chip=r[11], found=r[12],
                                                found_reason=r[13], city=r[14], district=r[15], ad_id=r[0])
            ads.append(ad)
        Log.logger.info('[DB] [AdManager] by filters %r for user %r has been gotten', *filters, user_id)
        return ads







m = AdManager()
#dog = asyncio.run(m.create_ad(type='found', species='Dog', name='Ben ', city='Moscow', district='Khimki', description='test descr 9', chip=False,
#                        location='23.23563.23563,4526.265', owner_id=252526, photo1_path='/home/spacecat/CODE/',
#                        photo2_path='/home/spacecat/CODE/', photo3_path='/home/spacecat/CODE/'))
#print(dog.name, dog.ad_id)
#lst = asyncio.run(m.get_user_ads(252526))
#print(lst[-1].name)
#asyncio.run(m.get_with_filters([{'name': 'species', 'value': 'Cat'}, {'name': 'type', 'value': 'lost'}]))