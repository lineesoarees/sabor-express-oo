from desafios.livro import Livro


livro_1 = Livro('Python orientado a objetos', 'Narcisa', 2020)
livro_2= Livro('Livro de culinária', 'Paola', 2019)

livro_1.emprestar()
print(livro_1.__str__())

