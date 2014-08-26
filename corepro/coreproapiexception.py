__author__ = 'socialmoneydev'

class CoreProApiException(object):
    def __init__(self, errors):
        self.errors = errors or []

    def firstMessage(self):
        return self.errors[0].message

    def firstCode(self):
        return self.errors[0].code

    def __repr__(self):
        msg = ''
        for e in self.errors:
            msg += repr(e) + ' '
        return msg

    def __str__(self):
        return repr(self)