class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('Vingadores', 2018, 160)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano}'
      f' - Temporadas: {vingadores.duracao}')

dexter = Serie('Dexter', 2008, 9)

print(f'Nome: {dexter.nome} - Ano: {dexter.ano}'
      f' - Temporadas: {dexter.temporadas}')
