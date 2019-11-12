# import tenis

############################################################################################
class Produto:
    def __init__(self,quantidade = None,valor = None, tenis = None):
        self.__tenis = tenis
        self.__quantidade = quantidade
        self.__valor = valor

    ### Os SETS ##################################################################
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def set_valor(self, valor):
        self.__valor = valor

    def set_tenis(self, tenis):
        self.__tenis = tenis

    ### Os GETS ##################################################################
    def get_quantidade(self):
        return self.__quantidade

    def get_valor(self):
        return self.__valor

    def get_tenis(self):
        return self.__tenis

#    def __str__(self):
#        retorno = "\n-------modelo:   " + str(self.__altura)
#        retorno += "\n-------numeração: " + str(self.__largura)
#        retorno += "\n-------cor:      " + str(self.__cor)
#        retorno += "\n-------quantidade: " + str(self.get_quantidade())
#        retorno += "\n-------valor " + str(self.get_valor())
#        return retorno

#        modelo = None, numeração = None, cor = None quantidade = None,valor