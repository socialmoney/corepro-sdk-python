__author__ = 'socialmoneydev'
from jsonBase import JsonBase

class FileContent(JsonBase):

    def __init__(self):
        self.content = None
        self.contentType = None
        self.contentLength = None
