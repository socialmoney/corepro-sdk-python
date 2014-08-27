__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from datetime import datetime

class Transaction(JsonBase):

    def __init__(self):
        self.requestId = None
        self.transactionCount = None
        self.customerId = None
        self.transactionId = None
        self.tag = None
        self.createdDate = None
        self.type = None
        self.typeCode = None
        self.status = None
        self.amount = None
        self.settledDate = None
        self.voidedDate = None
        self.nachaDescription = None
        self.friendlyDescription = None
        self.availableDate = None
        self.returnCode = None
        self.isCredit = None

    @staticmethod
    def listItems(customerId, accountId, status = None, beginDate = None, endDate = None, pageNumber = 0, pageSize = 200, connection = None, loggingObject = None):
        t = Transaction()
        t.customerId = customerId
        return t.list(accountId, status, beginDate, endDate, pageNumber, pageSize, connection, loggingObject)

    def list(self, accountId, status = None, beginDate = None, endDate = None, pageNumber = 0, pageSize = 200, connection = None, loggingObject = None):

        # normalize begin date
        start = None
        if isinstance(beginDate, datetime):
            start = beginDate.strftime('%Y-%m-%d')
        elif isinstance(beginDate, str):
            start = beginDate[:10]
        else:
            start = beginDate
        start = start or ''

        # normalize end date
        finish = None
        if isinstance(endDate, datetime):
            finish = endDate.strftime('%Y-%m-%d')
        elif isinstance(endDate, str):
            finish = endDate[:10]
        else:
            finish = endDate
        finish = finish or ''

        # if finish is given, force a default for start if it's not given
        if finish != '' and start == '':
            start = '1900-01-01'

        return Requestor().get("/transaction/list/{0}/{1}/{2}/{3}/{4}?pageNumber={5}&pageSize={6}".format(self.customerId, accountId, Requestor.escape(status), start, finish, pageNumber or 0, pageSize or 200), Transaction, connection, loggingObject)


