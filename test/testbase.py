__author__ = 'socialmoneydev'
import unittest
import sys, os

import os.path

class TestBase(unittest.TestCase):

    defaultRoot = sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'corepro'))

    prepaidCustomerId = None
    prepaidAccountId = None
    prepaidExternalAccountId = None
    prepaidCustomerBeneficiaryId = None


