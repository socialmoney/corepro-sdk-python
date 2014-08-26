from testbase import TestBase
from corepro.account import Account

class AbAccountTest(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        a = Account.getItem(2654, 2655)
        self.assertTrue(a.customerId == 2654)

    def test_list(self):
        accounts = Account.listItems(2654)
        self.assertTrue(len(accounts) > 0)
