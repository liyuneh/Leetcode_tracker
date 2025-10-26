class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 >= len(self.balance) or account2 >= len(self.balance):
            return False
        if self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account >= len(self.balance):
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account >= len(self.balance):
            return False
        if self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True


# Example usage:
# obj = Bank([100, 200, 300])
# print(obj.transfer(1, 2, 50))
# print(obj.deposit(3, 100))
# print(obj.withdraw(2, 150))
