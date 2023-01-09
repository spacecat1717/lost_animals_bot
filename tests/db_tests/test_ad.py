import asyncio
import asynctest

from datetime import date

from database.ads.ad import Ad


class DBAdTestCase(asynctest.TestCase):

    def setUp(self) -> None:
        self.ad = Ad(type='lost', owner_id=222545, species='Cat', location='23.23563.23563,4526.265',
                     creation_date=date(2023, 1, 8), photo2_path='/home/spacecat/CODE/',
                     photo1_path='/home/spacecat/CODE/', photo3_path='/home/spacecat/CODE/', name='random cat 2',
                     description='test descr 2', chip=False)

    async def test_set_found_attr(self) -> None:
        await self.ad.change_found(True, 'test found reason')
        self.assertTrue(self.ad.found)
        self.assertEqual(self.ad.found_reason, 'test found reason')
        await self.ad.change_found(False, '')
        self.assertFalse(self.ad.found)
        self.assertFalse(self.ad.found_reason)

    #TODO: add corner cases