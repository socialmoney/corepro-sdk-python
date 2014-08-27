__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class CustomerMessage(JsonBase):

    def __init__(self):
        self.verificationId = None
        self.verificationMessage = None
