from testbase import TestBase
from corepro.externalaccount import ExternalAccount

class TestAcExternalAccount(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        TestBase.prepaidExternalAccountId = 2666
        ea = ExternalAccount.getItem(TestBase.prepaidCustomerId, TestBase.prepaidExternalAccountId)
        self.assertTrue(ea.customerId == TestBase.prepaidCustomerId)

    def test_list(self):
        eas = ExternalAccount.listItems(TestBase.prepaidCustomerId)
        self.assertTrue(len(eas) > 0)
