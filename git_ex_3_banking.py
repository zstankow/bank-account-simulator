from random import randint


class Account:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.id = self.get_acc_num()

    def get_acc_num(self):
        self.id = "".join([str(randint(0,9)) for i in range(16)])
        return self.id

    def get_balance(self):
        return self.balance

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        if self.balance - num < 0:
            print(f"You do not have sufficient funds to withdraw {num} dollars.")
            print(f"The maximum amount you may withdraw is {self.balance}. Withdraw not completed.")
        else:
            self.balance -= num

    def acc_summary(self):
        print(f"Your account ID is {self.id} and your current balance is {self.balance} dollars.")


if __name__ == "__main__":
    acc1 = Account()
    id1 = acc1.get_acc_num()
    print(id1)
    assert acc1.get_balance() == 0
    acc1.deposit(100)
    assert acc1.get_balance() == 100
    acc1.withdraw(50)
    assert acc1.get_balance() == 50
    acc1.withdraw(60)
    assert acc1.get_balance() == 50
    acc1.acc_summary()







