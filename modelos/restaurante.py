from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title() # primeira maiuscula
        self.categoria= categoria.upper() # maisuculas
        self.idade = 0
        self._ativo= False #uso do _ para que essa propriedade não seja acessada, a não ser por @property
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}' 
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome Restaurante'.ljust(25)} |{'Categoria'.ljust(15)} |{'Avaliação'.ljust(10)}| {'Status'.ljust(10)}')
        for restauraunte in cls.restaurantes:
            print(f'{restauraunte.nome.ljust(25)} |{restauraunte.categoria.ljust(15)} |{str(restauraunte.media_avaliacoes).ljust(10)}| {restauraunte.ativo.ljust(10)}')    
        
    def alternar_estado(self):
        self._ativo = not self._ativo   
       
    def receber_avaliacao(self, cliente, nota, texto):
        if  nota < 0 or nota > 5:
            print('Nota inválida, digite uma nota de 0 a 5')
        else:
            avaliacao = Avaliacao(cliente, nota,texto)
            self._avaliacao.append(avaliacao)
    
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_notas= sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)
        media_notas = round(soma_notas/qtde_notas,1)
        return media_notas
    
#função dir(restaurante_1) mostra todos os atributos/métodos do objeto
#função vars(restaurante_1) mostra o conteúdo das variáveis do objeto