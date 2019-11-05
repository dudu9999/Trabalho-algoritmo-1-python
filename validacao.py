class Validacao:
    def __init__(self, cor):
        self.__cor = cor

    ### Validador de digitação de numero ##################################################################
    def lerInteiro(self, mens):
        while True:
            try:
                n = int(input(mens))
                return n
            except:
                input('...Erro. Você não digitou um número inteiro.')