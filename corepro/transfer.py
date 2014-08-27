__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor

class Transfer(JsonBase):

    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.fromId = None
        self.toId = None
        self.amount = None
        self.tag = None
        self.transactionId = None

    @staticmethod
    def createItem(customerId, fromId, toId, amount, tag, connection = None, loggingObject = None):
        t = Transfer()
        t.customerId = customerId
        t.fromId = fromId
        t.toId = toId
        t.amount = amount
        t.tag = tag
        return t.create(connection, loggingObject)

    def create(self, connection = None, loggingObject = None):
        return Requestor().post("/transfer/create", Transfer, self, connection, loggingObject)

    @staticmethod
    def voidItem(customerId, transactionId, tag, connection = None, loggingObject = None):
        t = Transfer()
        t.customerId = customerId
        t.transactionId = transactionId
        t.tag = tag
        return t.void(connection, loggingObject)

    def void(self, connection = None, loggingObject = None):
        return Requestor().post("/transfer/void", Transfer, self, connection, loggingObject)