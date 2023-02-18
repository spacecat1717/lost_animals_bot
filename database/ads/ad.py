"""Every ad is an instance of this class object"""

import asyncio

from datetime import date

from config.log_config import Logger as Log
from database.connection import Connection


class Ad:
    def __init__(self, type: str, owner_id=0, city='', district='', location='',
                 creation_date=date.today(), photo_path='', species='',
                 name='', description='', chip=False,
                 found=False, found_reason='', ad_id=None) -> None:
        self._connection = Connection()
        self._ad_id = ad_id
        self._type = type
        self._owner_id = owner_id
        self._city = city
        self._district = district
        self._location = location
        self._creation_date = creation_date
        self._photo_path = photo_path
        self._name = name
        self._species = species
        self._description = description
        self._chip = chip
        self._found = found
        self._found_reason = found_reason

    """Getters/Setters below"""

    def _get_ad_id(self) -> int:
        return self._ad_id

    def _set_ad_id(self, id: int) -> None:
        self._ad_id = id

    def _get_type(self) -> str:
        return self._type

    def _get_owner_id(self) -> int:
        return self._owner_id

    def _set_owner_id(self, value: int) -> None:
        self._owner_id = value

    def _get_type(self) -> str:
        return self._type

    def _get_city(self) -> str:
        return self._city

    def _set_city(self, value: str) -> None:
        self._city = value

    def _get_district(self) -> str:
        return self._district

    def _set_district(self, value: str) -> None:
        self._district = value

    def _get_location(self) -> str:
        return self._location

    def _set_location(self, value: str) -> None:
        self._location = value

    def _get_creation_date(self) -> date:
        return self._creation_date

    def _get_photo(self) -> str:
        return self._photo_path

    def _set_photo(self, path: str) -> None:
        self._photo_path = path

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, value: str) -> None:
        self._name = value

    def _get_species(self) -> str:
        return self._species

    def _set_species(self, value: str) -> None:
        self._species = value

    def _get_description(self) -> str:
        return self._description

    def _set_description(self, value: str) -> None:
        self._description = value

    def _get_chip(self) -> bool:
        return self._chip

    def _set_chip(self, value: bool) -> None:
        self._chip = value

    def _get_found(self) -> bool:
        return self._found

    def _get_found_reason(self) -> str:
        return self._found_reason

    def _set_found(self, value: bool) -> None:
        self._found = value

    def _set_found_reason(self, value: str) -> None:
        self._found_reason = value

    ad_id = property(_get_ad_id, _set_ad_id)
    type = property(_get_type)
    owner_id = property(_get_owner_id, _set_owner_id)
    type = property(_get_type)
    city = property(_get_city, _set_city)
    district = property(_get_district, _set_district)
    location = property(_get_location, _set_location)
    creation_date = property(_get_creation_date)
    photo = property(_get_photo, _set_photo)
    name = property(_get_name, _set_name)
    species = property(_get_species, _set_species)
    description = property(_get_description, _set_description)
    chip = property(_get_chip, _set_chip)
    found = property(_get_found, _set_found)
    found_reason = property(_get_found_reason, _set_found_reason)

    async def save_ad(self) -> bool:
        """Saving data in DB"""
        command = (
            "INSERT INTO ads(type, owner, city, district, location, date, photo1, name, species, description,\
            chip, found, found_reason) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13) RETURNING id"
        )
        try:
            async with self._connection as conn:
                values = (self._type, self.owner_id, self.city, self.district, self.location, self.creation_date,
                          self.photo, self.name, self.species, self.description, self.chip, self.found,
                          self.found_reason)
                res = await conn.fetch(command, *values)
                self.ad_id = res[0][0]
            Log.logger.info('[DB] Ad about animal %r has been created in DB', self.name)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create ad record about animal %r. reason: %r', self.name, e)
            return False

    async def delete_ad(self) -> bool:
        """Delete ad in DB"""
        command = (
            "DELETE FROM ads WHERE id = $1"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command, self.ad_id)
            Log.logger.info('[DB] Ad %r has been deleted', self.ad_id)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not delete ad %r. Reason: %r', self.ad_id, e)
            return False

    async def change_found(self, found: bool, found_reason: str) -> bool:
        command = (
            "UPDATE ads SET found=$1, found_reason=$2 WHERE id=$3"
        )
        try:
            self.found = found
            self.found_reason = found_reason
            async with self._connection as conn:
                await conn.execute(command, self.found, self.found_reason, self.ad_id)
            Log.logger.info('[DB] Found field for ad %r has been changed', self.ad_id)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not change found field for ad %r. Reason: %r', self.ad_id, e)
            return False


#a = Ad(type='lost', species='Other', name='random rat ', description='test descr 6', chip=False,
        #      location='23.23563.23563,4526.265', owner_id=222545, photo1_path='/home/spacecat/CODE/',
       #photo2_path='/home/spacecat/CODE/', photo3_path='/home/spacecat/CODE/', creation_date=date.today())
#asyncio.run(a.save_ad())
#print(a.ad_id)