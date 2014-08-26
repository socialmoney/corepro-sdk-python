__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class ApiError(JsonBase):
    def __init__(self):
        self.code = None
        self.message = None

    def __repr__(self):
        return "code: " + self.code + ", message: " + self.message

    def __str__(self):
        return repr(self)
