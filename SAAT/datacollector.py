from Tarefa import Tarefa

class Datas():

    def coletor(self):
        """Coletando dados"""
        tarefa = Tarefa().abrir()

        lista = ["ID", "Nome", "Importância", "Início", "Fim", "Duracao", "Data",
                 "Subtarefa"]  # Nome de todas as colunas do banco de dados
        dic = {}  # Dicionário relacionando as linhas e colunas do banco de dados
        l = []
        dicionario = []  # Dicionário relacionando todas as linhas e colunas do banco de dados

        for tupla in tarefa:

            for c, i in enumerate(tupla):
                lis = (lista[c] + ":", i)
                l.append(lis)

            dic = dict(l)
            dicionario.append(dic)

        return dicionario


