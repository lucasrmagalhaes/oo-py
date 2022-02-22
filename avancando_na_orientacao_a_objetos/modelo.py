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

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} like(s)')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} like(s)')

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

dexter = Serie('dexter', 2008, 9)

filmes_e_series = [vingadores, dexter]

for programa in filmes_e_series:
    programa.imprime()