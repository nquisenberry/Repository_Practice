class Checking_Account:
    def __init__(self,id_number,name,balance):
        self.id_number = id_number
        self.name = name
        self.balance = balance

    def print_details(self):
        print(self.id_number)
        print(self.name)
        print(self.balance)

    def deposit(self,value):
        self.balance = self.balance + value
    
nathan_Q = Checking_Account(12345, "Nathan q", 700.00)
nathan_Q.print_details()