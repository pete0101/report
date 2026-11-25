class Maksukortti:
    def __init__(self, saldo):
        self.saldo = saldo

    def osta(self, hinta):
        if self.saldo >= hinta:
            self.saldo -= hinta
            return True
        return False