from testbase import TestBase
from corepro.customerdocument import CustomerDocument
import os

class TestAeCustomerDocument(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upload(self):
        cd = CustomerDocument()
        cd.customerId = TestBase.prepaidCustomerId
        cd.documentType = 'DriversLicense'
        cd.reasonType = 'NameChange'
        cd.documentName = 'test.pdf'
        folder = os.path.dirname(os.path.abspath(__file__))
        filename = folder + os.path.sep + 'test.pdf'
        with open(filename, mode='rb') as f:
            cd.documentContent = f.read()
        cd.upload(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(True)
