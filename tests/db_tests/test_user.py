import asyncio
import asynctest

from database.connection import Connection
from database.user.user import User


class DbUserTestCase(asynctest.TestCase):

    def setUp(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.connection = Connection()
        self.user = User(tlg_id=22222, username='test user1')

    async def test_set_is_admin_attr(self) -> None:
        await self.user.change_admin(False)
        self.assertFalse(self.user.is_admin)
        await self.user.change_admin(True)
        self.assertTrue(self.user.is_admin)

    async def test_set_is_banned_attr(self) -> None:
        await self.user.change_ban(True)
        self.assertTrue(self.user.is_banned)
        await self.user.change_ban(False)
        self.assertFalse(self.user.is_banned)

