__author__ = 'socialmoneydev'

from jsonBase import JsonBase
from customermessage import CustomerMessage
from customerquestion import CustomerQuestion

class CustomerResponse(JsonBase):
    def __init__(self):
        self.customerId = None
        self.messages = []
        self.questions = []
        self.verificationId = None
        self.verificationStatus = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        classDefs['messages'] = CustomerMessage
        classDefs['questions'] = CustomerQuestion
        super(CustomerResponse, self).fromDict(self, dct, classDefs)

