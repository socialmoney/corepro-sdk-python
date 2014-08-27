__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class CustomerAnswer(JsonBase):

    def __init__(self):
        self.questionType = None
        self.questionAnswer = None
