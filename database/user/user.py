"""Every user is instance of User class"""
import asyncio

from config.log_config import Logger as Log
from database.connection import Connection

class User:
    def __init__(self, tlg_id: int, username: str, is_admin=False, is_banned=False) -> None:
        self._tlg_id = tlg_id
        self._username = username
        self._is_admin = is_admin
        self._is_banned = is_banned
        self._connection = Connection()

    """Getters/Setters below"""

    def _get_tlg_id(self) -> int:
        return self._tlg_id
    tlg_id = property(_get_tlg_id)

    def _get_username(self) -> str:
        return self._username
    username = property(_get_username)

    def _get_is_admin(self) -> bool:
        return self._is_admin

    def _set_is_admin(self, value: bool) -> None:
        self._is_admin = value

    is_admin = property(_get_is_admin, _set_is_admin)

    def _get_is_banned(self) -> bool:
        return self._is_banned

    def _set_is_banned(self, value: bool) -> None:
        self._is_banned = value

    is_banned = property(_get_is_banned, _set_is_banned)

    async def save_user(self) -> bool:
        """This method saves User data in DB"""
        command = (
            "INSERT INTO users(tlg_id, username, is_banned, is_admin) VALUES(\
            $1, $2, $3, $4)"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command, self.tlg_id, self.username, self.is_banned, self.is_admin)
            Log.logger.info('[DB] User %r has been saved in DB', self.tlg_id)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not save user %r in DB. Reason: %r', self.tlg_id, e)
            return False

    async def change_ban(self, value: bool) -> bool:
        command = (
            "UPDATE users SET is_banned=$1 WHERE tlg_id=$2"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command, value, self.tlg_id)
            self.is_banned = value
            Log.logger.info('[DB] Ban status of user %r has been changed', self.tlg_id)
            return True
        except Exception as e:
            Log.logger.error('[DB]Could not change ban status of user %r. Reason: %r', self.tlg_id, e)
            return False

    async def change_admin(self, value: bool) -> bool:
        command = (
            "UPDATE users SET is_admin=$1 WHERE tlg_id=$2"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command, value, self.tlg_id)
            self.is_admin = value
            Log.logger.info('[DB] Admin status of user %r has been changed', self.tlg_id)
            return True
        except Exception as e:
            Log.logger.error('[DB] Could not change admin status of user %r. Reason: %r', self.tlg_id, e)
            return False



#u = User(tlg_id=222545, username='test user2')
#asyncio.run(u.save_user())





