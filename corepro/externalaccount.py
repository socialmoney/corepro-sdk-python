__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.externalaccountidonly import ExternalAccountIdOnly
from models.externalaccountverify import ExternalAccountVerify

class ExternalAccount(JsonBase):

    def __init__(self):
        self.requestId = None
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
    def getItem(customerId, externalAccountId, connection = None, loggingObject = None):
        ea = ExternalAccount()
        ea.customerId = customerId
        ea.externalAccountId = externalAccountId
        return ea.get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/externalaccount/get/{0}/{1}".format(self.customerId, self.externalAccountId), ExternalAccount, connection, loggingObject)

    @staticmethod
    def getItemByTag(customerId, tag, connection = None, loggingObject = None):
        ea = ExternalAccount()
        ea.customerId = customerId
        ea.tag = tag
        return ea.getByTag(connection, loggingObject)

    def getByTag(self, connection = None, loggingObject = None):
        return Requestor().get("/externalaccount/getbytag/{0}/{1}".format(self.customerId, Requestor.escape(self.tag)), ExternalAccount, connection, loggingObject)

    def create(self, connection = None, loggingObject = None):
        eaid = Requestor().post("/externalaccount/create", ExternalAccountIdOnly, self, connection, loggingObject)
        return eaid.externalAccountId

    def initiate(self, connection = None, loggingObject = None):
        eaid = Requestor().post("/externalaccount/initiate", ExternalAccountIdOnly, self, connection, loggingObject)
        return eaid.externalAccountId

    @staticmethod
    def verifyItem(customerId, externalAccountId, amount1, amount2, connection = None, loggingObject = None):
        ea = ExternalAccount()
        ea.customerId = customerId
        ea.externalAccountId = externalAccountId
        return ea.verify()

    def verify(self, amount1, amount2, connection = None, loggingObject = None):
        eav = ExternalAccountVerify()
        eav.customerId = self.customerId
        eav.externalAccountId = self.externalAccountId
        eav.amount1 = amount1
        eav.amount2 = amount2
        return Requestor.post('/externalaccount/verify', eav, self)

    def update(self, connection = None, loggingObject = None):
        eaid = Requestor().post("/externalaccount/update", ExternalAccountIdOnly, self, connection, loggingObject)
        return eaid.externalAccountId

    def deactivate(self, connection = None, loggingObject = None):
        eaid = Requestor().post("/externalaccount/deactivate", ExternalAccountIdOnly, self, connection, loggingObject)
        return eaid.externalAccountId


