### Validador de digitação de numero ##################################################################
def lerInteiro(mens):
    while True:
        try:
            n = int(input(mens))
            return n
        except:
            input('...Erro. Você não digitou um número inteiro.')