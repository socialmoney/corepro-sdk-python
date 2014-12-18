__author__ = 'socialmoneydev'

from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.programlimit import ProgramLimit
from models.programchecking import ProgramChecking
from models.programecode import ProgramECode
from models.programprepaid import ProgramPrepaid
from models.programsavings import ProgramSavings

class Program(JsonBase):

    def __init__(self):
        self.requestId = None
        self.name = None
        self.verificationType = None
        self.timeZone = None
        self.perUserDailyWithdrawLimit = None
        self.perUserMonthlyWithdrawLimit = None
        self.perProgramDailyWithdrawLimit = None
        self.perUserDailyDepositLimit = None
        self.perUserMonthlyDepositLimit = None
        self.perProgramDailyDepositLimit = None
        self.website = None
        self.isInternalToInternalTransferEnabled = None
        self.decimalCount = None
        self.isInterestEnabled = None
        self.allowedAccountType = None
        self.isRecurringContributionEnabled = None
        self.filledDate = None
        self.perUserExternalAccountCountMax = None
        self.perUserAccountCountMax = None
        self.perUserTotalAccountBalanceMax = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()

        classDefs['perUserDailyWithdrawLimit'] = ProgramLimit
        classDefs['perUserMonthlyWithdrawLimit'] = ProgramLimit
        classDefs['perProgramDailyWithdrawLimit'] = ProgramLimit

        classDefs['perUserDailyDepositLimit'] = ProgramLimit
        classDefs['perUserMonthlyDepositLimit'] = ProgramLimit
        classDefs['perProgramDailyDepositLimit'] = ProgramLimit

        classDefs['checkingProducts'] = ProgramChecking
        classDefs['eCodeProducts'] = ProgramECode
        classDefs['prepaidProducts'] = ProgramPrepaid
        classDefs['savingsProducts'] = ProgramSavings

        super(Program, self).fromDict(dct, classDefs)

    @staticmethod
    def getItem(connection = None, loggingObject = None):
        return Program().get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/program/get", Program, connection, loggingObject)