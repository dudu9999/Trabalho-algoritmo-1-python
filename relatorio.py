import main

class Relatorio:
    def __init__(self, cor):
        self.__cor = cor

    ### Função Relatorio geral ##################################################################
    def relatorioGeral(self):
        for t in main.listaTenis:
            print('Tenis:', t.get_tenis())