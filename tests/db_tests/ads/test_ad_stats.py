import asynctest

from database.ads.ad_stats import AdStats, Ad


class DBAdStatsTestCase(asynctest.TestCase):
    def setUp(self) -> None:
        self.manager = AdStats()

    async def test_all_ads_quan(self) -> None:
        res = await self.manager.all_ads_quantity()
        self.assertIsInstance(res, int)
        self.assertTrue(res > 0)

    async def test_ads_quan_by_type_correct(self) -> None:
        res = await self.manager.ads_quantity_by_type('lost')
        self.assertIsInstance(res, int)
        self.assertTrue(res > 0)

    async def test_ads_quan_by_type_incorrect(self) -> None:
        res = await self.manager.ads_quantity_by_type('gggg')
        self.assertTrue(res == 0)

    async def test_ads_quan_by_species_correct(self) -> None:
        res = await self.manager.ads_quantity_by_species('Dog')
        self.assertIsInstance(res, int)
        self.assertTrue(res > 0)

    async def test_ads_quan_by_species_incorrect(self) -> None:
        res = await self.manager.ads_quantity_by_species('Rat')
        self.assertTrue(res == 0)

    async def test_ads_quan_by_found(self) -> None:
        res = await self.manager.ads_quantity_by_found(False)
        self.assertIsInstance(res, int)
        self.assertTrue(res > 1)

    async def test_last_ads(self) -> None:
        res = await self.manager.last_ads()
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)
        self.assertIsInstance(res[0], Ad)

