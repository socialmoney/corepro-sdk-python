__author__ = 'socialmoneydev'
from models.apierror import ApiError

class CoreProApiException(BaseException):
    def __init__(self, errors, status):
        self.errors = errors or []
        if (status != 200 and status != 201 and len(self.errors) == 0):
            ae = ApiError()
            ae.code = 50000 + int(status)
            ae.message = "HTTP Status {0} received".format(status)
            self.errors.append(ApiError)

    def firstMessage(self):
        return self.errors[0].message

    def firstCode(self):
        return self.errors[0].code

    def __str__(self):
        items = []
        for e in self.errors:
            items.append(str(e))
        return ''.join(items)
