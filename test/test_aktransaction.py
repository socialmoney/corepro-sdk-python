from testbase import TestBase
from corepro.transaction import Transaction

class TestAdCustomerBeneficiaryPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list(self):
        ts = Transaction.listItems(TestBase.prepaidCustomerId, TestBase.prepaidAccountId, None, None, None, None, None, TestBase.prepaidConn, TestBase.loggingObject)