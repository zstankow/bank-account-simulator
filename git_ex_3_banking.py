from random import randint


class Account:
    all_ids = {}

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.id = self.generate_acc_num()

    def generate_acc_num(self):
        """ Generates account number made up of four random digits when a new instance of Account is created.
            The account number is unique. """
        while True:
            new_acc_num = "".join([str(randint(0, 9)) for _ in range(6)])
            if new_acc_num not in Account.all_ids.values():
                Account.all_ids[self] = new_acc_num
                return new_acc_num

    def get_acc_num(self):
        """ Returns account number. """
        return Account.all_ids[self]

    def get_balance(self):
        """ Returns account balance. """
        return self.balance

    def deposit(self, num):
        """ Deposits specified sum into the account and updates the account balance. """
        self.balance += num

    def withdraw(self, num):
        """ Withdraws specified sum from the account and updates the account balance.
            If requested sum is greater than the existing balance, the withdrawal is not completed. """
        if self.balance - num < 0:
            print(f"You do not have sufficient funds to withdraw {num} dollars.")
            print(f"The maximum amount you may withdraw is {self.balance}. Withdrawal not completed.")
        else:
            self.balance -= num

    def acc_summary(self):
        """ Prints account summary including the account ID number and the current balance. """
        return f"Your account ID is {self.id} and your current balance is {self.balance} dollars."


def all_tests():
    # Creating a new instance of Account
    acc1 = Account()
    id1 = acc1.get_acc_num()
    # Check that get_acc_num() retrieves the ID of acc1 and does not regenerate
    assert acc1.get_acc_num() == id1
    # Check that the new instance was added to the class variable storing all accounts
    assert Account.all_ids == {acc1: id1}
    acc2 = Account()
    id2 = acc2.get_acc_num()
    # Check that the new instance was added to the class variable storing all accounts
    assert Account.all_ids == {acc1: id1, acc2: id2}
    # Check that the id for acc1 has not changed and can be retrieved from the class variable
    assert acc1.id == Account.all_ids[acc1]
    # Check that get_acc_num() retrieves the ID of acc2 and does not regenerate
    assert acc2.get_acc_num() == id2
    # Check that get_balance() returns 0, since there was no initial sum
    assert acc1.get_balance() == 0
    acc1.deposit(100)
    # Check that get_balance() returns 100 after the deposit
    assert acc1.get_balance() == 100
    acc1.withdraw(50)
    # Check that get_balance() returns 50 after the withdrawal
    assert acc1.get_balance() == 50
    acc1.withdraw(60)
    # Check that get_balance() returns 50 after the withdrawal failed since the requested sum was
    # larger than existing balance
    assert acc1.get_balance() == 50
    acc1.withdraw(10)
    # Check that get_balance() returns 40 after the withdrawal of 10
    assert acc1.get_balance() == 40

    assert acc1.acc_summary() == f'Your account ID is {acc1.id} and your current balance is {acc1.get_balance()} dollars.'
    assert acc2.acc_summary() == f'Your account ID is {acc2.id} and your current balance is {acc2.get_balance()} dollars.'


if __name__ == "__main__":
    all_tests()
