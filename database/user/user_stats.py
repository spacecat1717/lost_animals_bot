"""This class manage stats about users"""

import asyncio

from typing import List
from datetime import date, timedelta

from config.log_config import Logger as Log
from database.connection import Connection
from database.user.user import User


class UserStats:
    def __init__(self):
        self._connection = Connection()

    async def users_quantity(self) -> int:
        """:return users quantity for all the time"""
        command = (
            "SELECT COUNT (*) FROM users"
        )
        async with self._connection as conn:
            res = await conn.fetch(command)
            Log.logger.info('[DB] [UserStats] Users quantity for all the time has been executed')
            return res[0][0]

    async def last_users_quantity(self) -> int or False:
        """:return users quantity for last week"""
        date_list = [(date.today() - timedelta(days=i)) for i in range(0, 8)]
        command = (
            "SELECT COUNT (*) FROM users WHERE date=$1::date"
        )
        quantity = 0
        try:
            async with self._connection as conn:
                for d in date_list:
                    res = await conn.fetch(command, d)
                    quantity += res[0][0]
            print(res[0][0])
        except Exception as e:
            Log.logger.error('[DB] [UserStats] Could not execute quantity of last users. Reason: %r', e)
            return False

    async def all_users(self) -> List[User]:
        """:return all users as a List"""
        pass

    async def last_users(self) -> List[User]:
        """:return users for last week as a List"""
        pass

    async def banned(self) -> List[User]:
        """:return all banned users for all the time as a List"""
        pass

u = UserStats()
asyncio.run(u.last_users_quantity())
