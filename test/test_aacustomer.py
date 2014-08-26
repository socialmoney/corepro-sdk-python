from testbase import TestBase
from corepro.customer import Customer

class TestAaCustomer(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        TestBase.prepaidCustomerId = 2664
        c = Customer.getItem(TestBase.prepaidCustomerId)
        self.assertTrue(c.customerId == TestBase.prepaidCustomerId)
        self.assertTrue(len(c.accounts) > 0)

    def test_getByTag(self):
        c = Customer.getItemByTag('jfm2014-08-19 10:08:58 -0500')
        self.assertTrue(c.customerId == TestBase.prepaidCustomerId)

