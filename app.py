from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Los Mex', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('aline', 0, 'odiei')
restaurante_praca.receber_avaliacao('Helena', 10, 'muito bom')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da Cidade')
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_paozinho)
bebida_suco.aplicar_desconto(10)
prato_paozinho.aplicar_desconto() #nesta classe fixei o desconto então não tem parâmetro

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()