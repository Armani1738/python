class Account:

    def __int__(self, balance, name):
        self._balance = balance
        self._name = name

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_deposit(self, amount):
        if amount > 0:
            self._balance += amount
