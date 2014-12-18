__author__ = 'socialmoneydev'
from jsonBase import JsonBase
from programlimit import ProgramLimit
from programinterestrate import ProgramInterestRate

class ProgramChecking(JsonBase):

    def isHashedPayload(self):
        return True

    def __init__(self):
        self.category = None
        self.type = None
        self.balanceLimit = None
        self.interestRates = []
        self.isExternalWithdrawEnabled = None
        self.isInterestEnabled = None
        self.isRecurringContributionEnabled = None
        self.perTransactionDepositLimit = None
        self.perTransactionWithdrawLimit = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        classDefs['interestRates'] = ProgramInterestRate
        classDefs['perTransactionWithdrawLimit'] = ProgramLimit
        classDefs['perTransactionDepositLimit'] = ProgramLimit
        super(ProgramChecking, self).fromDict(dct, classDefs)


