class Restaurante:
    nome =''
    categoria=''
    ativo=False
    
#função dir(restaurante_1) mostra todos os atributos/métodos do objeto
#função vars(restaurante_1) mostra o conteúdo das variáveis do objeto

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Mamma mia'
restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))
status = 'Ativo'  if restaurante_praca.ativo else 'Inativo'
print(f'O restaurante {restaurante_praca.nome} está {status}')

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
