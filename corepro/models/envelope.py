__author__ = 'socialmoneydev'
from jsonBase import JsonBase
from apierror import ApiError

class Envelope(JsonBase):
    def __init__(self):
        self.data = None
        self.errors = []
        self.requestId = None
        self.status = None
        self.rawRequestBody = None
        self.rawResponseBody = None

    def fromJson(self, jsonData, classDefs):
        classDefs = classDefs or dict()
        classDefs['errors'] = ApiError
        super(Envelope, self).fromJson(jsonData, classDefs)

        if self.data is not None:
            if isinstance(self.data, list):
                for v in self.data:
                    if hasattr(v, 'requestId'):
                        v.requestId = self.requestId
            elif hasattr(self.data, 'requestId'):
                self.data.requestId = self.requestId

        return self
