from unittest import TestCase

from javapythonassignment.account import Account


class TestAccount(TestCase):
    def __int__(self):
        myAccount = Account()
        myAccount.set_balance(0)
        result = 0
        answer = myAccount.get_balance()
        self.assertEqual(result, answer)
