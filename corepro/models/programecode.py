__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ProgramECode(JsonBase):

    def isHashedPayload(self):
        return True

    def __init__(self):
        self.category = None
        self.type = None
        self.programECodeId = None
        self.productCode = None
        self.minimumAmount = None
        self.maximumAmount = None
        self.name = None
        self.imageUrl = None
        self.isReissueSupported = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        super(ProgramECode, self).fromDict(dct, classDefs)
