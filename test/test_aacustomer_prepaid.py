from testbase import TestBase
from corepro.customer import Customer

class TestAaCustomerPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        c = Customer()
        c.birthDate = '01/01/1985'
        c.culture = 'en-US'
        c.firstName = 'Svetlana'
        c.middleName = 'Dyevochka'
        c.lastName = "Beerlady" + TestBase.timestamp
        c.gender = 'F'
        c.isDocumentsAccepted = True
        c.isSubjectToBackupWithholding = False
        c.isOptedInToBankCommunication = False
        c.tag = "sdb python " + TestBase.timestamp
        c.taxId = '900000283'

        TestBase.prepaidCustomerId = c.create(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidCustomerId > 0)

    def test_get(self):
        c = Customer.getItem(TestBase.prepaidCustomerId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(c.customerId == TestBase.prepaidCustomerId)

    def test_getByTag(self):
        c = Customer.getItemByTag("sdb python " + TestBase.timestamp, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(c.customerId == TestBase.prepaidCustomerId)

    def test_list(self):
        cs = Customer.listItems(0, 200, TestBase.prepaidConn, TestBase.loggingObject)

    def test_search(self):
        c = Customer()
        c.lastName = 'Beerlady' + TestBase.timestamp
        cs = c.search(0, 200, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(len(cs) == 1)

    def test_update(self):
        c = Customer()
        c.customerId = TestBase.prepaidCustomerId
        c.firstName = "Svetlana" + TestBase.timestamp
        customerId = c.update(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(customerId > 0)

    def test_zzz_deactivate(self):
        pass