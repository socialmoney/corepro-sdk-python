__author__ = 'socialmoneydev'
from customeranswer import CustomerAnswer
from jsonBase import JsonBase

class CustomerQuestion(JsonBase):

    def __init__(self):
        self.answers = []
        self.prompt = None
        self.type = None

    def fromDict(self, dct, classDefs):
        classDefs = classDefs or dict()
        classDefs['answers'] = CustomerAnswer
        super(CustomerQuestion, self).fromDict(dct, classDefs)