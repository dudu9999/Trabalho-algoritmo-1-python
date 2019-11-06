
### Criação da Classe Tenis ###############################################
class Tenis:
    def __init__(self, modelo, numeração, , cor):
        self.__modelo = modelo
        self.__numeração = numeração
        self.__cor = cor

    ### Os SETS ##################################################################
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_numeração(self, numeração):
        self.__numeração = numeração

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def set_valor(self, valor):
        self.__valor = valor

    def set_cor(self, cor):
        self.__cor = cor

    ### Os GETS ##################################################################
    def get_modelo(self):
        return self.__modelo

    def get_numeração(self):
        return self.__numeração

    def get_quantidade(self):
        return self.__quantidade

    def get_valor(self):
        return self.__valor

    def get_cor(self):
        return self.__cor

