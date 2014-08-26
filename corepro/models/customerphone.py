__author__ = 'socialmoneydev'

from jsonBase import JsonBase

class CustomerPhone(JsonBase):

    def __init__(self):
        self.phoneType = None
        self.number = None
        self.isActive = None

