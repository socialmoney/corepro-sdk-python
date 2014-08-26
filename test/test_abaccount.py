from testbase import TestBase
from corepro.account import Account

class TestAbAccount(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        TestBase.prepaidAccountId = 2665
        a = Account.getItem(TestBase.prepaidCustomerId, TestBase.prepaidAccountId)
        self.assertTrue(a.customerId == TestBase.prepaidCustomerId)

    def test_list(self):
        accounts = Account.listItems(TestBase.prepaidCustomerId)
        self.assertTrue(len(accounts) > 0)
