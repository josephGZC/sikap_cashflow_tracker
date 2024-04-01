class Transaction:
    def __init__(self, date, kind, category, name, amount, account) -> None:
        self.date = date
        self.kind = kind
        self.category = category
        self.name = name
        self.amount = amount
        self.account = account
       
    def __repr__(self):
        return f"<Transaction: {self.date},{self.kind},{self.category},{self.name},₱{self.amount:.2f},{self.account}>"


