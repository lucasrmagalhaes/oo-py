class Relatorio:
    def gera_relatorio(self):
        print('Relatório geral')

class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatório dos usuários')

class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatório de custos')

relatorio_usuarios = RelatorioUsuarios()
relatorio_custos = RelatorioCustos()

relatorios = [relatorio_usuarios, relatorio_custos]

for rel in relatorios:
    rel.gera_relatorio()