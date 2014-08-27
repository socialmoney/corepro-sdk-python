__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
import base64

class CustomerDocument(JsonBase):

    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.documentType = None
        self.documentName = None
        self.documentContent = None
        self.reasonType = None

    @staticmethod
    def uploadDocument(customerId, documentType, documentName, documentContent, reasonType, connection = None, loggingObject = None):
        cd = CustomerDocument()
        cd.customerId = customerId
        cd.documentType = documentType
        cd.documentName = documentName
        cd.documentContent = documentContent
        cd.reasonType = reasonType
        return cd.upload(connection, loggingObject)

    def upload(self, connection = None, loggingObject = None):
        # NOTE: documentContent is assumed to be raw content bytes.
        #       corepro API expects base64 encoded string. so we convert that here.
        self.documentContent = base64.b64encode(self.documentContent)
        return Requestor().post("/customerdocument/upload", None, self, connection, loggingObject)