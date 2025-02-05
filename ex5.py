class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError('Balance cannot be negative.')
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive.')
        if amount > self.balance:
            raise ValueError('Not enough money to withdraw.')
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Balance: {self.balance}'


# Testy, które konwencjonalnie powinny znajdoać się w osobnym pliku
# testowym, ale dla uproszczenia umieszczam je tutaj:

import unittest

class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.get_balance(), 100)

    def test_initial_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount(-100)
    
    def test_deposit(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_deposit_negative_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw(self):
        account = BankAccount(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_negative_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_withdraw_more_than_balance(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(150)
    

if __name__ == '__main__':
    unittest.main()
