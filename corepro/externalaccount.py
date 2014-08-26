__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor

class ExternalAccount(JsonBase):

    def __init__(self):
        self.externalAccountId = None
        self.customerId = None
        self.tag = None
        self.name = None
        self.routingNumber = None
        self.accountNumber = None
        self.type = None
        self.nickName = None
        self.status = None
        self.statusDate = None
        self.nocCode = None
        self.isActive = None
        self.isLocked = None
        self.lockedDate = None
        self.lockedReason = None


    @staticmethod
    def listItems(customerId, connection = None, loggingObject = None):
        ea = ExternalAccount()
        ea.customerId = customerId
        return ea.list(connection, loggingObject)

    def list(self, connection = None, loggingObject = None):
        rv = Requestor().get("/externalaccount/list/{0}".format(self.customerId), ExternalAccount, connection, loggingObject)
        return rv

    @staticmethod
    def getItem(customerId, accountId, connection = None, loggingObject = None):
        ea = ExternalAccount()
        ea.customerId = customerId
        ea.accountId = accountId
        return ea.get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        rv = Requestor().get("/externalaccount/get/{0}/{1}".format(self.customerId, self.accountId), ExternalAccount, connection, loggingObject)
        return rv

