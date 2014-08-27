__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ProgramInterestRate(JsonBase):

    def __init__(self):
        self.tier = None
        self.apy = None
        self.apr = None
        self.minimumAmount = None
        self.maximumAmount = None

    def __str__(self):
        return "tier: {0}, apy: {1}, apr: {2}, min: {3}, max: {4}".format(self.tier, self.apy, self.apr, self.min, self.max)