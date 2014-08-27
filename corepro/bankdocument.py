__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.filecontent import FileContent

class BankDocument(JsonBase):

    def __init__(self):
        self.requestId = None
        self.bankId = None
        self.customerId = None
        self.documentId = None
        self.documentType = None
        self.culture = None
        self.html = None
        self.title = None
        self.downloadUrl = None
        self.effectiveDate = None
        self.expireDate = None

    @staticmethod
    def listItems(culture, documentType = None, connection = None, loggingObject = None):
        bd = BankDocument()
        bd.culture = culture
        bd.documentType = documentType
        return bd.list(connection, loggingObject)

    def list(self, connection = None, loggingObject = None):
        return Requestor().get("/bankdocument/list/{0}/{1}".format(Requestor.escape(self.culture), Requestor.escape(self.documentType)), BankDocument, connection, loggingObject)

    @staticmethod
    def downloadItem(culture, documentId = None, connection = None, loggingObject = None):
        bd = BankDocument()
        bd.culture = culture
        bd.documentId = documentId
        return bd.download(connection, loggingObject)

    def download(self, connection = None, loggingObject = None):
        return Requestor().get("/bankdocument/download/{0}/{1}".format(Requestor.escape(self.culture), self.documentId), FileContent, connection, loggingObject)
