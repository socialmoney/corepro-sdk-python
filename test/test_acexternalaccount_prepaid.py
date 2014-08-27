from testbase import TestBase
from corepro.externalaccount import ExternalAccount

class TestAcExternalAccountPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        ea = ExternalAccount()
        ea.customerId = TestBase.prepaidCustomerId
        ea.nickName = "Ext acct " + TestBase.timestamp
        ea.tag = "tag " + TestBase.timestamp
        ea.accountNumber = '00001234'
        ea.firstName = 'Jimmy'
        ea.lastName = 'Jameson'
        ea.type = 'Client'
        TestBase.prepaidExternalAccountId = ea.create(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidExternalAccountId > 0)

    def test_get(self):
        ea = ExternalAccount.getItem(TestBase.prepaidCustomerId, TestBase.prepaidExternalAccountId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(ea.externalAccountId == TestBase.prepaidExternalAccountId)

    def test_getbytag(self):
        ea = ExternalAccount.getItemByTag(TestBase.prepaidCustomerId, "tag " + TestBase.timestamp, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(ea.externalAccountId == TestBase.prepaidExternalAccountId)

    def test_list(self):
        eas = ExternalAccount.listItems(TestBase.prepaidCustomerId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(len(eas) > 0)

    def test_update(self):
        ea = ExternalAccount()
        ea.customerId = TestBase.prepaidCustomerId
        ea.externalAccountId = TestBase.prepaidExternalAccountId
        ea.nickName = "Updated ext act " + TestBase.timestamp
        externalAccountId = ea.update(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidExternalAccountId == externalAccountId)

    def test_zzz_deactivate(self):
        pass
