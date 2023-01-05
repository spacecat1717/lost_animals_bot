"""Every ad is an instance of this class object"""

import asyncio

from datetime import date

from config.log_config import Logger as Log
from database.connection import Connection


class Ad:
    def __init__(self, type: str, owner_id: int, location: str, creation_date: date, photo1_path: str,
                 photo2_path: str, photo3_path: str, name: str, species: str, description: str, chip: bool,
                 found=False, found_reason='') -> None:
        self._connection = Connection()
        self._type = type
        self._owner_id = owner_id
        self._location = location
        self._creation_date = creation_date
        self._photo_path1 = photo1_path
        self._photo_path2 = photo2_path
        self._photo_path3 = photo3_path
        self._name = name
        self._species = species
        self._description = description
        self._chip = chip
        self._found = found
        self._found_reason = found_reason

    """Getters/Setters below"""

    def _get_type(self) -> str:
        return self._type

    def _get_owner_id(self) -> int:
        return self._owner_id

    def _get_type(self) -> str:
        return self._type

    def _get_location(self) -> str:
        return self._location

    def _get_creation_date(self) -> date:
        return self._creation_date

    def _get_photos(self) -> tuple:
        return self._photo_path1, self._photo_path2, self._photo_path3

    def _get_name(self) -> str:
        return self._name

    def _get_speceies(self) -> str:
        return self._species

    def _get_description(self) -> str:
        return self._description

    def _get_chip(self) -> bool:
        return self._chip

    def _get_found(self) -> bool:
        return self._found

    def _get_found_reason(self) -> str:
        return self._found_reason

    def _set_found(self, value: bool) -> None:
        self._found = value

    def _set_found_reason(self, value: str) -> None:
        self._found_reason = value

    type = property(_get_type)
    owner_id = property(_get_owner_id)
    type = property(_get_type)
    location = property(_get_location)
    creation_date = property(_get_creation_date)
    photos = property(_get_photos)
    name = property(_get_name)
    species = property(_get_speceies)
    description = property(_get_description)
    chip = property(_get_chip)
    found = property(_get_found, _set_found)
    found_reason = property(_get_found_reason, _set_found_reason)

    async def create_ad(self) -> bool:
        """Saving data in DB"""
        command = (
            "INSERT INTO ads(type, owner, location, date, photo1, photo2, photo3, name, species, description,\
            chip, found, found_reason) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)"
        )
        try:
            async with self._connection as conn:
                values = (self._type, self.owner_id, self.location, self.creation_date, self.photos[0], self.photos[1],
                          self.photos[2], self.name, self.species, self.description, self.chip, self.found,
                          self.found_reason)
                await conn.execute(command, *values)
            Log.logger.info('[DB] Ad about animal %r has been created in DB', self.name)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create ad record about animal %r. reason: %r', self.name, e)
            return False


#a = Ad(type='lost', species='Cat', name='random cat', description='test descr', chip=False,
#       location='23.23563.23563,4526.265', owner_id=22222, photo1_path='/home/spacecat/CODE/',
#       photo2_path='/home/spacecat/CODE/', photo3_path='/home/spacecat/CODE/', creation_date=date.today())
#asyncio.run(a.create_ad())
