class Musica:
    musicas = []
    def __init__(self, nome='', compositor='', duracao=0):
        
        self.nome = nome
        self.compositor = compositor
        self.duracao = duracao
        Musica.musicas.append(self)
        
    def listar_musicas():
        for musica in Musica.musicas:
            print(f' {musica.nome} | {musica.compositor}')

Musica('Bang', 'Anitta', 'Pop')   
Musica('Rajadão', 'Pablo Vittar', 'Pop')   

Musica.listar_musicas()
        