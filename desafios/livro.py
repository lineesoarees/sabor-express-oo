class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
        
    def __str__(self):
        disponivel = 'Sim' if self.disponivel else 'Não'
        return f'Livro: {self.titulo}. Autor: {self.autor}. Ano: {self.ano}; Disponível: {disponivel}'
    
    def emprestar(self):
       self.disponivel = False
       return self.disponivel
    
 
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano == ano :
                livros_disponiveis.append(livro)        
        return livros_disponiveis

disponiveis = []
disponiveis = Livro.verificar_disponibilidade(2020)
for livro in disponiveis:
    print(f'{livro.titulo} do ano {livro.ano} está disponível')