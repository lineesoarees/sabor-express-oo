class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        
    def __str__(self):
        ligado = 'Sim' if self._ligado else 'Não'
        return f'Modelo: {self.modelo}| Marca: {self.marca}| Ligado: {ligado}'