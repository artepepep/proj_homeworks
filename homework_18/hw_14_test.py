class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'
    
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        self._balance += interest

    def __str__(self):
        return f'Savings Account number: {self._account_number}, balance: {self._balance}'
    
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Overdraft Letter sent for Account {self._account_number}")

    def __str__(self):
        return f'Current Account number: {self._account_number}, balance: {self._balance}'
    
class Bank:
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def close_account(self, account_number):
        self._accounts = [acc for acc in self._accounts if acc.get_account_number() != account_number]

    def pay_dividend(self, amount):
        for account in self._accounts:
            account.deposit(amount)

    def update_accounts(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def __str__(self):
        return '\n'.join(map(str, self._accounts))