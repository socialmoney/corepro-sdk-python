__author__ = 'socialmoneydev'
import sys, os
import unittest
import datetime
from corepro.connection import Connection

class TestBase(unittest.TestCase):

    defaultRoot = sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'corepro'))
    timestamp = str(datetime.datetime.now())
    loggingObject = None

    prepaidConn = Connection.createFromConfig()
    prepaidCustomerId = None
    prepaidAccountId = None
    prepaidExternalAccountId = None
    prepaidCustomerBeneficiaryId = None

    bankDocumentId = None


