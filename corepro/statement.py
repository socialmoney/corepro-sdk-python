__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.filecontent import FileContent

class Statement(JsonBase):

    def __init__(self):
        self.requestId = None
        self.statementId = None
        self.customerId = None
        self.type = None
        self.month = None
        self.year = None

    @staticmethod
    def getItem(customerId, statementId, connection = None, loggingObject = None):
        return Requestor().get("/statement/get/{0}/{1}".format(customerId, statementId), Statement, connection, loggingObject)

    @staticmethod
    def listItems(customerId, connection = None, loggingObject = None):
        return Requestor().get("/statement/list/{0}".format(customerId), Statement, connection, loggingObject)

    @staticmethod
    def downloadItem(customerId, statementId, connection = None, loggingObject = None):
        return Requestor.get("/statement/download/{0}/{1}".format(customerId, statementId), FileContent, connection, loggingObject)