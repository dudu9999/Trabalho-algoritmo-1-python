listaModeloExemplo = ('Tradicional', 'Esportivo', 'Caminhada', 'Corrida')
listaCorExemplo = ['Branco', 'Azul', 'Amarelo', 'Vermelho']

### Validador de digitação de numero ##################################################################
def lerInteiro():
    while True:
        try:
            n = int(input('Digite um numero: '))
            return n
        except:
            input('...Erro. Você não digitou um número inteiro.')

### Função para mostra o menu ###################################################################
def menu():
    menu = '''
------------------------------------------------------------------
    Menu
    0-  Sair
    1-  Cadastrar Tenis
    2-  Relatório Geral
    3-  Realizar Venda
    4-  Atualizar preços
    5-  Cadastrar Cores
    6-  Guarda no TXT
    7-  Recupera do TXT'''
    return print(menu)

### mostra a lista de exemplo ##############################################################
def mostraListaExemplo(listaExemplo):
    ind = 0
    for x in listaExemplo:
        print('  ' + str(ind) + ' - ' + listaExemplo[ind])
        ind += 1
    print('')

def validaCadastroModelo():
    mostraListaExemplo(listaModeloExemplo)
    escolha = str(input("Modelo: "))
    if escolha == '1':
        modelo = 'Tradicional'
    if escolha == '2':
        modelo = 'Esportivo'
    if escolha == '3':
        modelo = 'Caminhada'
    if escolha == '4':
        modelo = 'Corrida'
    return modelo

### Função de cadastro Numeracao ##################################################################
def validaCadastroNumeracao():
    n = lerInteiro("Numeração: ")
    return n

### Função de cadastro Quantidade ##################################################################
def validaCadastroQuantidade():
    q = lerInteiro("Quantidade: ")
    return q

### Função de cadastro Valor ##################################################################
def validaCadastroValor():
    v = lerInteiro("Valor: ")
    return v

### Função de cadastro Cor ##################################################################
def validaCadastroCor():
    mostraListaExemplo(listaCorExemplo)
    c = input("Cor: ")
    return c