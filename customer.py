from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custSaldo = 10000):
        self.id = id
        self.custPin = custPin
        self.custSaldo = custSaldo

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.custPin

    def checkSaldo(self):
        return self.custSaldo

    def debet(self, nominal):
        self.custSaldo -= nominal

    def simpan(self, nominal):
        self.custSaldo += nominal

    def changePin(self, pin):
        self.custPin = pin