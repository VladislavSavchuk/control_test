"""Создайте класс "Банковский счет" с методами для внесения и снятия денег, а также для проверки баланса.
Учтите возможность возникновения ошибок при операциях со счетом"""


class BankAccount:
    def __init__(self, deposit_amount=0):
        self.balance = deposit_amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Счет должен быть положительный")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Счет должен быть положительный")
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"Депозит создан. На Вашем счету: {self.balance}$"


try:
    account = BankAccount(100)
    print(account)
    print(f"Начальный депозит: {account.check_balance()}")

    account.deposit(50)
    print(f"Баланс после пополнения счета: {account.check_balance()}")

    account.withdraw(20)
    print(f"Баланс после снятия денег со счета: {account.check_balance()}")
except ValueError as e:
    print(e)
