"""This class can manage User objects"""

import asyncio

from datetime import date

from config.log_config import Logger as Log
from database.connection import Connection
from database.user.user import User


class UserManager:
    def __init__(self):
        self._connection = Connection()

    async def create_user(self, user_id: int, username: str) -> User or False:
        """Creates user record in DB
        :return User instance"""
        user = await self._create_user_obj(user_id, username, is_admin=False, is_banned=False, date=date.today())
        if not await user.save_user():
            return False
        return user

    @staticmethod
    async def _create_user_obj(user_id: int, username: str, is_admin: bool, is_banned: bool, date: date) -> User:
        """Creates only User object"""
        user = User(tlg_id=user_id, username=username, is_admin=is_admin, is_banned=is_banned, date=date)
        return user

    async def delete_user(self, user: User) -> bool:
        return await user.delete_user()

    async def get_user(self, user_id: int) -> User or False:
        """Gets user's record from DB, creates its instance"""
        command = (
            "SELECT tlg_id, username, is_admin, is_banned, date FROM users WHERE tlg_id=$1"
        )
        try:
            async with self._connection as conn:
                res = await conn.fetch(command, user_id)
            Log.logger.info('[DB] [UserManager] Data of user %r has been executed', user_id)
            user = await self._create_user_obj(user_id=user_id, username=res[0][1],
                                               is_admin=res[0][2], is_banned=res[0][3], date=res[0][4])
            return user
        except IndexError:
            Log.logger.error('[DB] [UserManager] User %r does not exists', user_id)
            return False

#m = UserManager()
#user = asyncio.run(m.create_user(788445, 'test user 2'))
#print(user.date)
