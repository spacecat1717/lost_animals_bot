import asynctest

from datetime import date

from database.ads.ad import Ad


class DBAdTestCase(asynctest.TestCase):

    def setUp(self) -> None:
        self.ad = Ad(type='lost', owner_id=222545, species='Cat', location='23.23563.23563,4526.265',
                     creation_date=date(2023, 1, 8), photo_path='/home/spacecat/CODE/', name='random cat 2',
                     description='test descr 2', chip=False)
        self.ad_for_deletion = Ad(type='lost', owner_id=66666, species='Cat', location='23.23563.23563,4526.265',
                                  creation_date=date.today(), photo_path='/home/spacecat/CODE/',
                                  name='random cat 5',  description='test descr 2', chip=False)

    async def test_set_found_attr(self) -> None:
        await self.ad.change_found(True, 'test found reason')
        self.assertTrue(self.ad.found)
        self.assertEqual(self.ad.found_reason, 'test found reason')
        await self.ad.change_found(False, '')
        self.assertFalse(self.ad.found)
        self.assertFalse(self.ad.found_reason)

    async def test_save_ad(self) -> None:
        self.assertTrue(self.ad_for_deletion.save_ad())

    async def test_delete_ad(self) -> None:
        self.assertTrue(self.ad_for_deletion.delete_ad())

