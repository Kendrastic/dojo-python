from unicodedata import name


class User:
    bank_name = "First Cat National Bank"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Your First Cat National Balance is: \n {self.account_balance}.")
        return self

# Create 3 instances of the User Class: Mike, Sara, Kendra
mike = User("Mike", "mike@aol.com")
sara = User("Sara", "sara@aol.com")
kendra = User("Kenda", "kendra@aol.com")


#Have Mike make 3 deposits and one withdrawal and then display balance
mike.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(111).display_user_balance()


#Have Sara make 2 deposits and 2 withdrawals and then display balance
sara.make_deposit(25).make_deposit(25).make_withdrawal(3).make_withdrawal(10).display_user_balance()

#Have Kendra make 1 deposit and 3 withdrawals and display balance
kendra.make_deposit(5000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()