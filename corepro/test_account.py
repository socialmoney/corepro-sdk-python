from unittest import TestCase
from account import Account

__author__ = 'socialmoneydev'


class TestAccount(TestCase):
    def test_list(self):
        a = Account()
        a.customerId = 2654
        a.list()

    def test_get(self):
        pass