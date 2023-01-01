"""this module creates all tables in DB oon startup"""

import asyncio

from config.log_config import Logger as Log
from database.connection import Connection


class CreateTables:
    def __init__(self) -> None:
        self._connection = Connection()

    async def create_users_table(self) -> bool:
        command = (
            "CREATE TABLE IF NOT EXISTS users(\
            id SERIAL,\
            tlg_id BIGINT,\
            username VARCHAR(64),\
            is_admin BOOL,\
            is_banned BOO;,\
            CONSTRAINT unique_tlg_id UNIQUE (tlg_id)\
            )"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command)
            Log.logger.info('[DB] Table users has been created')
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create table users. Reason: ', e)
            return False


