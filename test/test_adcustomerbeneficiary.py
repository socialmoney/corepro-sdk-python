from testbase import TestBase
from corepro.customerbeneficiary import CustomerBeneficiary

class TestAdCustomerBeneficiaryPrepaid(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create(self):
        cb = CustomerBeneficiary()
        cb.customerId = TestBase.prepaidCustomerId
        cb.firstName = 'Freddie'
        cb.lastName = "Mercury Python " + TestBase.timestamp
        cb.birthDate = '1969-05-05T00:00:00.000+00:00'
        cb.taxId = '123412349'
        TestBase.prepaidCustomerBeneficiaryId = cb.create(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidCustomerBeneficiaryId > 0)

    def test_get(self):
        cb = CustomerBeneficiary.getItem(TestBase.prepaidCustomerId, TestBase.prepaidCustomerBeneficiaryId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(cb.customerBeneficiaryId == TestBase.prepaidCustomerBeneficiaryId)

    def test_list(self):
        cbs = CustomerBeneficiary.listItems(TestBase.prepaidCustomerId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(len(cbs) > 0)

    def test_update(self):
        cb = CustomerBeneficiary()
        cb.customerId = TestBase.prepaidCustomerId
        cb.customerBeneficiaryId = TestBase.prepaidCustomerBeneficiaryId
        cb.firstName = "Freddie " + TestBase.timestamp
        cbid = cb.update(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(TestBase.prepaidCustomerBeneficiaryId == cbid)

    def test_zzz_deactivate(self):
        pass