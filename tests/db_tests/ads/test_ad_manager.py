import asynctest

from database.ads.ad_manager import AdManager, Ad


class DBAdManagerTestCase(asynctest.TestCase):

    def setUp(self) -> None:
        self.manager = AdManager()
        self.test_id = 252526
        self.test_filter1 = [{'name': 'type', 'value': 'lost'}]
        self.test_filter2 = [{'name': 'species', 'value': 'Dog'}, {'name': 'city', 'value': 'Moscow'}]
        self.test_filter3 = [{'name': 'species', 'value': 'Rat'}]

    async def test_create_ad(self) -> None:
        ad = await self.manager.create_ad(type='lost', species='Dog', name='test dog', city='Moscow', district='Butovo',
                                          description='test descr', chip=True, location='23.23563.23563,4526.265',
                                          owner_id=self.test_id, photo_path='/home/spacecat/CODE/')
        self.assertTrue(ad)

    async def test_get_existing_user_ads(self) -> None:
        res = await self.manager.get_user_ads(self.test_id)
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)
        self.assertIsInstance(res[0], Ad)

    async def test_get_not_existing_user_ads(self) -> None:
        res = await self.manager.get_user_ads(1111111)
        self.assertFalse(res)

    async def test_get_ads_with_one_filter(self) -> None:
        res = await self.manager.get_with_filters(self.test_filter1)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Ad)
        self.assertTrue(len(res) > 1)

    async def test_get_ads_with_two_filters(self) -> None:
        res = await self.manager.get_with_filters(self.test_filter2)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], Ad)
        self.assertTrue(len(res) > 1)

    async def test_get_ads_with_wrong_filter(self) -> None:
        res = await self.manager.get_with_filters(self.test_filter3)
        self.assertFalse(res)
