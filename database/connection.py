"""this module creates connection to DB using Singleton class"""

import asyncpg

from config import config
from config.log_config import Logger as Log


class Connection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Connection, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):

        if (self.__initialized):
            return
        self.__initialized = True
        self._db_name = config.DB_NAME
        self._db_user = config.DB_USER
        self._db_password = config.DB_PASS
        self._db_host = config.DB_HOST
        self._conn = None
        Log.logger.info('[DB] [CONNECTION] Connection instance has been created')

    async def _get_conn(self):
        return self._conn

    conn = property(_get_conn)

    async def __aenter__(self):
        self._conn = await asyncpg.connect(database=self._db_name, user=self._db_user, password=self._db_password,
                                           host=self._db_host)
        return self._conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._conn.close()
