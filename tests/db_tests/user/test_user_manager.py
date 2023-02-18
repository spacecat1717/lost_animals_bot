import asynctest

from datetime import date
from random import randint

from database.user.user_manager import UserManager


class DBUserManagerTestCase(asynctest.TestCase):
    def setUp(self) -> None:
        self.manager = UserManager()
        self.test_id = randint(0, 10000)

    async def test_create_user(self) -> None:
        user = await self.manager.create_user(self.test_id, 'mr black')
        self.assertTrue(user)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_banned)
        self.assertEqual(user.date, date.today())

    async def test_get_existing_user(self) -> None:
        user = await self.manager.get_user(17171717)
        self.assertTrue(user)
        self.assertEqual(user.username, 'spacecat')

    async def test_get_not_existing_user(self) -> None:
        self.assertFalse(await self.manager.get_user(1111111))
        self.assertLogs('root', 'ERROR')