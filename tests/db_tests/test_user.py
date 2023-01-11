import asyncio
import asynctest

from database.user.user import User


class DbUserTestCase(asynctest.TestCase):

    def setUp(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.user = User(tlg_id=22222, username='test user1', is_admin=True, is_banned=False)
        self.user_for_deletion = User(tlg_id=66666, username='user for deletion')

    async def test_get_attrs(self) -> None:
        self.assertTrue(self.user.is_admin)
        self.assertFalse(self.user.is_banned)

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

    async def test_save_user(self) -> None:
        self.assertTrue(await self.user_for_deletion.save_user())

    async def test_delete_user(self) -> None:
        self.assertTrue(await self.user_for_deletion.delete_user())


