__author__ = 'socialmoneydev'

from jsonBase import JsonBase

class CustomerAddress(JsonBase):

    def __init__(self):
        self.addressType = None
        self.addressLine1 = None
        self.addressLine2 = None
        self.addressLine3 = None
        self.addressLine4 = None
        self.city = None
        self.state = None
        self.postalCode = None
        self.country = None
        self.isActive = None
