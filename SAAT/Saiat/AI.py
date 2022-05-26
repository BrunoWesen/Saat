"""
Essa IA não tem o propósito de ser super inteligente, é somente para "degustação"
-------------------------------------------------------------------------------
this AI has no purpose of be inteligent, its only for "degustation"
"""

import numpy as np

tarefas = (1, 'Lavar o gato', 6, '17:40', '17:51', 12, '31/12/2020', 'sub')


class Ai:
    def __init__(self, dados):  # Esses dados devem vir em formato de tupla
        self.dados = dados
        # print(self.dados)

    def importancia(self):  # Definindo os tempos que se deve focar em cada importância
        imp = self.dados[2]

        if imp <= 5:
            print("Hoi")

        if imp > 5:
            print("Hui")

        return 0


if __name__ == "__main__":
    AI = Ai(tarefas).importancia()
