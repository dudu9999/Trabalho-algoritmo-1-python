import tenis

############################################################################################
class Produto:
    def __init__(self,quantidade,valor, produto):
        self.produto = produto
        self.__quantidade = quantidade
        self.__valor = valor

        ### Os SETS ##################################################################
        def set_quantidade(self, quantidade):
            self.__quantidade = quantidade

        def set_valor(self, valor):
            self.__valor = valor

        def set_produto(self, produto):
            self.__produto = produto

        ### Os GETS ##################################################################
        def get_quantidade(self):
            return self.__quantidade

        def get_valor(self):
            return self.__valor

        def get_produto(self):
            return self.__produto

