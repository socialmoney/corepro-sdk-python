__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
import base64

class ExternalAccountDocument(JsonBase):

    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.externalAccountId = None
        self.documentType = None
        self.documentName = None
        self.documentContent = None
        self.reasonType = None

    @staticmethod
    def uploadDocument(customerId, externalAccountId, documentType, documentName, documentContent, reasonType, connection = None, loggingObject = None):
        ead = ExternalAccountDocument()
        ead.customerId = customerId
        ead.externalAccountId = externalAccountId
        ead.documentType = documentType
        ead.documentName = documentName
        ead.documentContent = documentContent
        ead.reasonType = reasonType
        return ead.upload(connection, loggingObject)

    def upload(self, connection = None, loggingObject = None):
        # NOTE: documentContent is assumed to be raw content bytes.
        #       corepro API expects base64 encoded string. so we convert that here.
        self.documentContent = base64.b64encode(self.documentContent)
        return Requestor().post("/externalaccountdocument/upload", None, self, connection, loggingObject)