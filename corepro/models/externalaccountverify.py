__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ExternalAccountVerify(JsonBase):

    def __init__(self):
        self.customerId = None
        self.externalAccountId = None
        self.amount1 = None
        self.amount2 = None
