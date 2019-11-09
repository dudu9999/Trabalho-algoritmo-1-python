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

def validaCadastroModelo():
    print('-- Modelo --')
    mostraListaExemplo(listaModeloExemplo)
    while True:
        escolha = str(input("Escolha um: "))
        if escolha == '1':
            return 'Tradicional'
        elif escolha == '2':
            return 'Esportivo'
        elif escolha == '3':
            return 'Caminhada'
        elif escolha == '4':
            return 'Corrida'
        else:
            print('Item inexistente digite o numero do item acima.')


### Função de cadastro Numeracao ##################################################################
def validaCadastroNumeracao():
    print()
    print('-- Numeração --')
    n = lerInteiro()
    return n

### Função de cadastro Quantidade ##################################################################
def validaCadastroQuantidade():
    print()
    print('-- Quantidade --')
    q = lerInteiro()
    return q

### Função de cadastro Valor ##################################################################
def validaCadastroValor():
    print()
    print('-- Valor --')
    v = lerInteiro()
    return v

### Função de cadastro Cor ##################################################################
def validaCadastroCor():
    print()
    print('-- Cor --')
    mostraListaExemplo(listaCorExemplo)
    while True:
        escolha = str(lerInteiro())
        if escolha == '1':
            return 'Tradicional'
        elif escolha == '2':
            return 'Esportivo'
        elif escolha == '3':
            return 'Caminhada'
        elif escolha == '4':
            return 'Corrida'
        else:
            print('Item inexistente digite o numero do item acima.')