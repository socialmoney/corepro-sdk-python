from testbase import TestBase
from corepro.transfer import Transfer

class TestAjTransferPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_external_to_internal(self):
        t = Transfer()
        t.customerId = TestBase.prepaidCustomerId
        t.fromId = TestBase.prepaidExternalAccountId
        t.toId = TestBase.prepaidAccountId
        t.amount = 1.25
        t.tag = "tag python " + TestBase.timestamp
        results = t.create(TestBase.prepaidConn, TestBase.loggingObject)
        TestBase.prepaidExternalToInternalTransactionId = results[0].transactionId
        self.assertTrue(TestBase.prepaidExternalToInternalTransactionId > 0)

    def test_create_internal_to_external(self):
        t = Transfer()
        t.customerId = TestBase.prepaidCustomerId
        t.fromId = TestBase.prepaidAccountId
        t.toId = TestBase.prepaidExternalAccountId
        t.amount = 1.20
        t.tag = "tag 2 python " + TestBase.timestamp
        results = t.create(TestBase.prepaidConn, TestBase.loggingObject)
        TestBase.prepaidInternalToExternalTransactionId = results[0].transactionId
        self.assertTrue(TestBase.prepaidInternalToExternalTransactionId > 0)

