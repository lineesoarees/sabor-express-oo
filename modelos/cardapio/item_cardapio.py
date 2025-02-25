from abc import ABC, abstractmethod #importamos para criar metodos abstratos na classe

class ItemCardapio(ABC):
    def __init__(self, nome, preco ):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass #não faz nada aqui porque é só para definir que todas as classes derivadas precisam ter este método obrigatoriamente
             # Bebida e Prato conceito de polimorfismo