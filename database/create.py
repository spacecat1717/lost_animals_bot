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
            tlg_id BIGINT NOT NULL,\
            username VARCHAR(64),\
            is_admin BOOL,\
            is_banned BOOL,\
            date DATE,\
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

    async def create_ads_table(self) -> bool:
        command = (
            "CREATE TABLE IF NOT EXISTS ads(\
            id SERIAL,\
            type VARCHAR(8),\
            owner BIGINT NOT NULL,\
            city VARCHAR(128),\
            district VARCHAR(128),\
            district VARCHAR(128),\
            location TEXT,\
            date DATE,\
            photo1 TEXT,\
            name VARCHAR(64) NOT NULL,\
            species VARCHAR(16) NOT NULL,\
            description TEXT,\
            chip BOOL,\
            found BOOL,\
            found_reason VARCHAR(32),\
            CONSTRAINT fk_owner FOREIGN KEY(owner) REFERENCES users(tlg_id) ON DELETE CASCADE\
            )"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command)
            Log.logger.info('[DB] Table ads has been created')
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create table ads. Reason ', e)
            return False


c = CreateTables()
#asyncio.run(c.create_users_table())
#asyncio.run(c.create_ads_table())