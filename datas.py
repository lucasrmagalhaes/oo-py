class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
        # print("{}/{}/{}".format(self.dia, self.mes,self.ano))
