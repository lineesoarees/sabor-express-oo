from desafios.agencia_veiculos.modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, nportas):
        super().__init__(marca, modelo)
        self.nportas = nportas
        
    def __str__(self):        
        return super().__str__()+f'| Portas: {self.nportas}'