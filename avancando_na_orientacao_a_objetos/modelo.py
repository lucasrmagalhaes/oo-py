class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
      f' - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}')

dexter = Serie('dexter', 2008, 9)
dexter.dar_like()

print(f'Nome: {dexter.nome} - Ano: {dexter.ano}'
      f' - Temporadas: {dexter.temporadas} - Likes: {dexter.likes}')
