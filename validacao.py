class Validacao:
    def __init__(self, cor):
        self.__cor = cor

    ### Validador de digitação de numero ##################################################################
    def lerInteiro(self):
        while True:
            try:
                n = int(input('Digite um numero: '))
                return n
            except:
                input('...Erro. Você não digitou um número inteiro.')