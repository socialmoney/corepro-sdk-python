__author__ = 'socialmoneydev'
from models.jsonBase import JsonBase
from utils.requestor import Requestor
from models.customerbeneficiaryidonly import CustomerBeneficiaryIdOnly

class CustomerBeneficiary(JsonBase):
    def __init__(self):
        self.requestId = None
        self.customerId = None
        self.customerBeneficiaryId = None
        self.firstName = None
        self.lastName = None
        self.birthDate = None
        self.taxId = None
        self.taxIdMasked = None
        self.isActive = None

    @staticmethod
    def listItems(customerId, connection = None, loggingObject = None):
        cb = CustomerBeneficiary()
        cb.customerId = customerId
        return cb.list(connection, loggingObject)

    def list(self, connection = None, loggingObject = None):
        return Requestor().get("/customerbeneficiary/list/{0}".format(self.customerId), CustomerBeneficiary, connection, loggingObject)

    @staticmethod
    def getItem(customerId, customerBeneficiaryId, connection = None, loggingObject = None):
        cb = CustomerBeneficiary()
        cb.customerId = customerId
        cb.customerBeneficiaryId = customerBeneficiaryId
        return cb.get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/customerbeneficiary/get/{0}/{1}".format(self.customerId, self.customerBeneficiaryId), CustomerBeneficiary, connection, loggingObject)

    def create(self, connection = None, loggingObject = None):
        cbid = Requestor().post("/customerbeneficiary/create", CustomerBeneficiaryIdOnly, self, connection, loggingObject)
        return cbid.customerBeneficiaryId

    def update(self, connection = None, loggingObject = None):
        cbid = Requestor().post("/customerbeneficiary/update", CustomerBeneficiaryIdOnly, self, connection, loggingObject)
        return cbid.customerBeneficiaryId

    def deactivate(self, connection = None, loggingObject = None):
        cbid = Requestor().post("/customerbeneficiary/deactivate", CustomerBeneficiaryIdOnly, self, connection, loggingObject)
        return cbid.customerBeneficiaryId
