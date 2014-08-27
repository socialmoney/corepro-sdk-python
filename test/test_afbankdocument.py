from testbase import TestBase
from corepro.bankdocument import BankDocument
from corepro.models.filecontent import FileContent

class TestAfBankDocument(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list(self):
        bds = BankDocument.listItems('en-US', None, TestBase.prepaidConn, TestBase.loggingObject)
        for a in bds:
            if a.documentType == 'eStatement':
                TestBase.bankDocumentId = a.documentId
        self.assertTrue(TestBase.bankDocumentId is not None)

    def test_zzz_download(self):
        fc = BankDocument.downloadItem('en-US', TestBase.bankDocumentId, TestBase.prepaidConn, TestBase.loggingObject)
        self.assertIsInstance(fc, FileContent)