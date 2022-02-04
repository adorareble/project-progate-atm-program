class ATMCard:
    def __init__(self, defaultPin, defaultSaldo):
        self.defaultPin = defaultPin
        self.defaultSaldo = defaultSaldo

    def cekPin(self):
        return self.defaultPin

    def cekSaldo(self):
        return self.defaultSaldo

