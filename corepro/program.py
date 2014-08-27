__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.programinterestrate import ProgramInterestRate
from models.programlimit import ProgramLimit
import base64

class Program(JsonBase):

    def __init__(self):
        self.requestId = None
        self.name = None
        self.verificationType = None
        self.timeZone = None
        self.regDFeeAmount = None
        self.regDMonthlyTransactionWithdrawCountMax = None
        self.perTransactionWithdrawLimit = None
        self.perUserDailyWithdrawLimit = None
        self.perUserMonthlyWithdrawLimit = None
        self.perProgramDailyWithdrawLimit = None
        self.perTransactionDepositLimit = None
        self.perUserDailyDepositLimit = None
        self.perUserMonthlyDepositLimit = None
        self.perProgramDailyDepositLimit = None
        self.website = None
        self.isInternalToInternalTransferEnabled = None
        self.decimalCount = None
        self.isInterestEnabled = None
        self.allowedAccountType = None
        self.isRecurringContributionEnabled = None
        self.interestRates = []
        self.filledDate = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        classDefs['interestRates'] = ProgramInterestRate

        classDefs['perTransactionWithdrawLimit'] = ProgramLimit
        classDefs['perUserDailyWithdrawLimit'] = ProgramLimit
        classDefs['perUserMonthlyWithdrawLimit'] = ProgramLimit
        classDefs['perProgramDailyWithdrawLimit'] = ProgramLimit

        classDefs['perTransactionDepositLimit'] = ProgramLimit
        classDefs['perUserDailyDepositLimit'] = ProgramLimit
        classDefs['perUserMonthlyDepositLimit'] = ProgramLimit
        classDefs['perProgramDailyDepositLimit'] = ProgramLimit

        super(Program, self).fromDict(dct, classDefs)

    @staticmethod
    def getItem(connection = None, loggingObject = None):
        return Program().get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/program/get", Program, connection, loggingObject)