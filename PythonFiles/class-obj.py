class  Bank:
    def __init__(self, name, branch, starting_balance: float = 1000.00) -> None:
        self.name = name
        self.branch = branch
        self.networth = starting_balance

bank1 = Bank('Zenith', 593,)
bank2 = Bank('Kuda', 0o33)
bank3 = Bank('Opay', 739)

print(bank1.name, bank1.branch, bank1.networth)
print(bank2.name, bank2.branch)
print(bank3.name, bank3.branch)



