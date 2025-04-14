class BankAccount:
    def __init__(self, account_holder):
        # BankAccount のメソッドは self._balance にアクセスできるが、
        # クラス外のコードからはアクセスできない
        self._balance = 0
        self._name = account_holder
        with open(f"{self._name}Ledger.txt", "w") as ledger_file:
            ledger_file.write("Balance is 0\n")
    
    def deposit(self, amount):
        if amount <= 0:
            return  # マイナスの残高は不可
        self._balance += amount
        with open(f"{self._name}Ledger.txt", "a") as ledger_file:
            ledger_file.write(f"Deposit {amount}\n")
            ledger_file.write(f"Balace is {self._balance}\n")
    
    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  # 残高不足もしくは引き出し額がマイナス
        self._balance -= amount
        with open(f"{self._name}Ledger.txt", "a") as ledger_file:
            ledger_file.write(f"Withdraw {amount}\n")
            ledger_file.write(f"Balance is {self._balance}\n")


acct = BankAccount("Alice")  # アリスの口座を作成
acct.deposit(120)            # deposit() で _balance が変更される
acct.withdraw(40)            # withdraw() で _balance が変更される

# BankAccount 外で _name や _balance を変更できるけれども、してはダメ
acct._balance = 1000000000
acct.withdraw(1000)

acct._name = "Bob"   # ボブの台帳に変えちゃう！
acct.withdraw(1000)  # 出勤記録が BobLedger.txt に記録されちゃう！
