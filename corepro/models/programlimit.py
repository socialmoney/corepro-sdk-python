__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ProgramLimit(JsonBase):

    def __init__(self):
        self.minimumAmount = None
        self.maximumAmount = None

    def __str__(self):
        return "min: {0}, max: {1}".format(self.minimumAmount, self.maximumAmount)
