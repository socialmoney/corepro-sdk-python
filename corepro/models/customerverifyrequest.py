__author__ = 'socialmoneydev'
from jsonBase import JsonBase
from customeranswer import CustomerAnswer
from customerresponse import CustomerResponse
from ..utils.requestor import Requestor

class CustomerVerifyRequest(JsonBase):

    def __init__(self):
        self.customerId = None
        self.verificationId = None
        self.answers = []

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        classDefs['answers'] = CustomerAnswer
        super(CustomerVerifyRequest, self).fromDict(dct, classDefs)

    def verify(self, connection = None, loggingObject = None):
        return Requestor.post('/customer/verify', CustomerResponse, self, connection, loggingObject)
