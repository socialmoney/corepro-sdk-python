__author__ = 'socialmoneydev'
from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.accountidonly import AccountIdOnly
from accountclose import AccountClose

class Account(JsonBase) :

    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.accountId = None
        self.tag = None
        self.name = None
        self.accountNumber = None
        self.accountNumberMasked = None
        self.routingNumber = None
        self.status = None
        self.type = None
        self.createdDate = None
        self.closedDate = None
        self.accountBalance = None
        self.availableBalance = None
        self.isPrimary = None
        self.isCloseable = None
        self.recurringContributionType = None
        self.recurringContributionAmount = None
        self.recurringContributionFromExternalAccountId = None
        self.recurringContributionStartDate = None
        self.recurringContributionEndDate = None
        self.recurringContributionNextDate = None
        self.targetAmount = None
        self.targetDate = None
        self.category = None
        self.subCategory = None
        self.miscellaneous = None

    @staticmethod
    def listItems(customerId, connection = None, loggingObject = None):
        a = Account()
        a.customerId = customerId
        return a.list(connection, loggingObject)

    def list(self, connection = None, loggingObject = None):
        rv = Requestor().get("/account/list/{0}".format(self.customerId), Account, connection, loggingObject)
        return rv

    @staticmethod
    def getItem(customerId, accountId, connection = None, loggingObject = None):
        a = Account()
        a.customerId = customerId
        a.accountId = accountId
        return a.get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/account/get/{0}/{1}".format(self.customerId, self.accountId), Account, connection, loggingObject)

    @staticmethod
    def getItemByTag(customerId, tag, connection = None, loggingObject = None):
        a = Account()
        a.customerId = customerId
        a.tag = tag
        return a.getByTag(connection, loggingObject)

    def getByTag(self, connection = None, loggingObject = None):
        return Requestor().get("/account/getbytag/{0}/{1}".format(self.customerId, Requestor.escape(self.tag)), Account, connection, loggingObject)

    def update(self, connection = None, loggingObject = None):
        aid = Requestor().post("/account/update", AccountIdOnly, self, connection, loggingObject)
        return aid.accountId

    def create(self, connection = None, loggingObject = None):
        aid = Requestor().post("/account/create", AccountIdOnly, self, connection, loggingObject)
        return aid.accountId

    def close(self, closeToAccountId, transactionTag, connection = None, loggingObject = None):
        ac = AccountClose()
        ac.closeToAccountId = closeToAccountId
        ac.transactionTag = transactionTag
        return ac.close(connection, loggingObject)