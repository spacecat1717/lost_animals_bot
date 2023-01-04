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

    async def lost_animals(self) -> bool:
        command = (
            "CREATE TABLE IF NOT EXISTS lost_animals(\
            id SERIAL,\
            owner BIGINT,\
            location TEXT,\
            date DATE,\
            photo1 TEXT,\
            photo2 TEXT,\
            photo3 TEXT,\
            name VARCHAR(64) NOT NULL,\
            species VARCHAR(16) NOT NULL,\
            description TEXT,\
            chip BOOL,\
            found BOOL,\
            found_reason VARCHAR(32)\
            CONSTRAINT fk_owner_lost FOREIGN KEY(owner) REFERENCES users(id)\
            )"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command)
            Log.logger.info('[DB] Table lost_animals has been created')
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create table lost_animals. Reason:  ', e)
            return False

    async def found_animals(self) -> bool:
        command = (
            "CREATE TABLE IF NOT EXISTS found_animals(\
                id SERIAL,\
                owner BIGINT,\
                location TEXT,\
                date DATE,\
                photo1 TEXT,\
                photo2 TEXT,\
                photo3 TEXT,\
                name VARCHAR(64) NOT NULL,\
                species VARCHAR(16) NOT NULL,\
                description TEXT,\
                chip BOOL,\
                found BOOL,\
                found_reason VARCHAR(32)\
                CONSTRAINT fk_owner_found FOREIGN KEY(owner) REFERENCES users(id)\
                )"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command)
            Log.logger.info('[DB] Table found_animals has been created')
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not create table found_animals. Reason: ', e)
            return False
