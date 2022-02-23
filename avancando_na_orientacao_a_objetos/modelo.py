class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} like(s)')

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} like(s)'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} like(s)'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} like(s)'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
dexter = Serie('dexter', 2008, 9)
tmep = Filme('Todo Mundo em Pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
dexter.dar_like()
dexter.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, dexter, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)