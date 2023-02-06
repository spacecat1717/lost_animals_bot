"""This class manage stats about ads"""

import asyncio

from typing import List
from datetime import date, timedelta

from config.log_config import Logger as Log
from database.connection import Connection
from database.ads.ad import Ad


class AdStats:

    def __init__(self):
        self._connection = Connection()

    async def all_ads_quantity(self) -> int:
        command = (
            "SELECT COUNT(*) FROM ads"
        )
        async with self._connection as conn:
            res = await conn.fetch(command)
        Log.logger.info("[DB] [AdStats] Ads quantity for all the time received")
        return res[0][0]

    async def ads_quantity_by_type(self, type: str) -> int:
        command = (
            "SELECT COUNT(*) FROM ads WHERE type=$1"
        )
        async with self._connection as conn:
            res = await conn.fetch(command, type)
        Log.logger.info('[DB] [AdStats] Ads quantity for all the time by type %r received', type)
        return res[0][0]

    async def ads_quantity_by_species(self, species: str) -> int:
        command = (
            "SELECT COUNT(*) FROM ads WHERE species=$1"
        )
        async with self._connection as conn:
            res = await conn.fetch(command, species)
        Log.logger.info('[DB] [AdStats] Ads quantity for all the time by species %r received')
        return res[0][0]

    async def last_ads(self) -> List[Ad]:
        date_list = [(date.today() - timedelta(days=i)) for i in range(0, 8)]
        command = (
            "SELECT * FROM ads WHERE date=$1::date"
        )
        ads_data: List[list] = []
        ads: List[Ad] = []
        async with self._connection as conn:
            for d in reversed(date_list):
                res = await conn.fetch(command, d)
                if res:
                    ads_data.extend(res)
            for a in ads_data:
                ads.append(Ad(ad_id=a[0], type=a[1], owner_id=a[2], location=a[3], creation_date=a[4], photo1_path=a[5],
                              photo2_path=a[6], photo3_path=a[7], name=a[8], species=a[9], description=a[10], chip=a[11],
                              found=a[12], found_reason=a[13], city=a[14], district=a[15]))
            Log.logger.info('[DB] [AdStats] Ads for the last 7 days received')
            return ads

    async def ads_quantity_by_found(self, found: bool) -> int:
        command = (
            "SELECT COUNT(*) FROM ads WHERE found=$1"
        )
        async with self._connection as conn:
            res = await conn.fetch(command, found)
        Log.logger.info('[DB] [AdStats] Quantity of ads with found=%r received', found)
        return res[0][0]





#m = AdStats()
#print(asyncio.run(m.ads_quantity_by_found(False)))
