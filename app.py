from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Los Mex', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('aline', 0, 'odiei')
restaurante_praca.receber_avaliacao('Helena', 10, 'muito bom')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()