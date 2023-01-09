import asyncio
import asynctest
import asyncpg

from database.connection import Connection


class DBConnectionTestCase(asynctest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    async def test_singleton(self):
        conn1 = Connection()
        conn2 = Connection()
        self.assertEqual(conn1, conn2)

    async def test_conn_attr(self):
        conn = Connection()
        async with conn as c:
            self.assertEqual(type(c), asyncpg.connection.Connection)



