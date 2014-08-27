__author__ = 'socialmoneydev'

from utils.requestor import Requestor
from models.jsonBase import JsonBase

class AccountClose(JsonBase):

    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.accountId = None
        self.closeToAccountId = None
        self.transactionId = None
        self.transactionTag = None
        self.closingBalanceAmount = None
        self.interestPaidAmount = None
        self.totalClosingAmount = None
        self.isClosedToExternalAccount = None

    def close(self, connection = None, loggingObject = None):
        return Requestor().post('/account/close', AccountClose, self, connection, loggingObject)
