import asynctest

from database.user.user_stats import UserStats, User


class DBUseStatsTestCase(asynctest.TestCase):
    def setUp(self) -> None:
        self.manager = UserStats()

    async def test_all_quan(self) -> None:
        res = await self.manager.users_quantity()
        self.assertIsInstance(res, int)
        self.assertTrue(res > 0)

    async def test_last_users_quan(self) -> None:
        res = await self.manager.last_users_quantity()
        self.assertIsInstance(res, int)
        self.assertTrue(res > 0)

    async def test_all_users_list(self) -> None:
        res = await self.manager.all_users()
        self.assertTrue(len(res) > 0)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], User)

    async def test_last_users_list(self) -> None:
        res = await self.manager.last_users()
        self.assertTrue(len(res) > 0)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], User)

    async def test_banned(self) -> None:
        res = await self.manager.banned()
        self.assertIsInstance(res, list)
