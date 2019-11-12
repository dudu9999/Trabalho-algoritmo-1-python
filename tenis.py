import validacao

### Criação da Classe Tenis ###############################################
class Tenis:
    def __init__(self, modelo = None, numeracao = None, cor = None):
        self.__modelo = modelo
        self.__numeracao = numeracao
        self.__cor = cor

    ### Os SETS ##################################################################
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_numeracao(self, numeracao):
        self.__numeracao = numeracao

    def set_cor(self, cor):
        self.__cor = cor

    ### Os GETS ##################################################################
    def get_modelo(self):
        return self.__modelo

    def get_numeracao(self):
        return self.__numeracao

    def get_cor(self):
        return self.__cor

