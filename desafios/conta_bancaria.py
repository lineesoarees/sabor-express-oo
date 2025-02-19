class Conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
        
    def __str__(self):
        msg_ativo = 'Ativa' if self._ativo else 'Inativa'
        return f'Titular da Conta: {self.titular} | Saldo da Conta: {self.saldo} | Conta {msg_ativo}'
    

    def ativa_inativa(cls):
        cls._ativo = not cls._ativo
        
conta_aline = Conta_bancaria('Aline',1000)
conta_helena = Conta_bancaria('Helena', 2000)

print(conta_aline.__str__())
conta_helena.ativa_inativa()
print(conta_helena.__str__())