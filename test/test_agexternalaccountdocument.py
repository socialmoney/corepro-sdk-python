from testbase import TestBase
from corepro.externalaccountdocument import ExternalAccountDocument
import os

class TestAgExternalAccountDocument(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upload(self):
        ead = ExternalAccountDocument()
        ead.customerId = TestBase.prepaidCustomerId
        ead.externalAccountId = TestBase.prepaidExternalAccountId
        ead.documentType = 'DriversLicense'
        ead.reasonType = 'NameChange'
        ead.documentName = 'test.pdf'
        folder = os.path.dirname(os.path.abspath(__file__))
        filename = folder + os.path.sep + 'test.pdf'
        with open(filename, mode='rb') as f:
            ead.documentContent = f.read()
        ead.upload(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(True)
