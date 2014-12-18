__author__ = 'bweaver'
from jsonBase import JsonBase
from programlimit import ProgramLimit
from programinterestrate import ProgramInterestRate

class ProgramPrepaid(JsonBase):

    def isHashedPayload(self):
        return True

    def __init__(self):
        self.category = None
        self.type = None
        self.balanceLimit = None
        self.interestRates = []
        self.isImmediateLoadFromLinkedAccountEnabled = None
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
        super(ProgramPrepaid, self).fromDict(dct, classDefs)
