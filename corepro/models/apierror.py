__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ApiError(JsonBase):
    def __init__(self):
        self.code = None
        self.message = None

    def __str__(self):
        return "code: {0}, message: {1}".format(self.code, self.message)
