from testbase import TestBase
from corepro.account import Account

class TestAbAccountPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        a = Account()
        a.customerId = TestBase.prepaidCustomerId
        a.tag = "act" + TestBase.timestamp
        a.type = 'Client'
        a.category = 'CategoryA'
        a.subCategory = 'CategoryB'
        a.isCloseable = True
        a.name = "Account " + TestBase.timestamp
        a.targetAmount = 500
        a.targetDate = '01/01/2030'
        TestBase.prepaidAccountId = a.create(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidAccountId > 0)

    def test_get(self):
        a = Account.getItem(TestBase.prepaidCustomerId, TestBase.prepaidAccountId, TestBase.prepaidConn, TestBase.timestamp)
        self.assertTrue(a.customerId == TestBase.prepaidCustomerId)

    def test_list(self):
        accounts = Account.listItems(TestBase.prepaidCustomerId, TestBase.prepaidConn, TestBase.timestamp)
        self.assertTrue(len(accounts) > 0)

    def test_update(self):
        #a = Account.getItem(TestBase.prepaidCustomerId, TestBase.prepaidAccountId, TestBase.prepaidConn, TestBase.loggingObject)
        a = Account()
        a.accountId = TestBase.prepaidAccountId
        a.customerId = TestBase.prepaidCustomerId
        a.name = "Updated account " + TestBase.timestamp
        accountId = a.update(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(accountId == TestBase.prepaidAccountId)
