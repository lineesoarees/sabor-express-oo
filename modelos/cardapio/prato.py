from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):           #classe super como parametro -> Herança
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #utiliza o construtor da classe principal, manter padrão e mesmos atributos obrigatórios
        self.descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)