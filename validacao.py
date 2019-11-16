# Trabalho - Utilizando Listas
# Autor:  Eduardo Caetano

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
------------------------------------------------------------
 --- Menu ---
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

### Função de cadastro de modelo ##################################################################
def validaCadastroModelo():
    print('-- Modelo --')
    mostraListaExemplo(listaModeloExemplo)
    while True:
        try:
            escolha = lerInteiro()
            if listaModeloExemplo[escolha] in listaModeloExemplo:
                m = listaModeloExemplo[escolha]
                return m
                break
        except:
            print('Item inexistente digite o numero do item acima.')

### Função de cadastro Numeracao ##################################################################
def validaCadastroNumeracao():
    print()
    print('-- Numeração --')
    n = lerInteiro()
    if n >= 22 and n <= 46:
        return n
    else:
        print('Erro - o numero digitado deve estar entre 22 e 46.')

### Função de cadastro Quantidade ##################################################################
def validaCadastroQuantidade():
    print()
    print('-- Quantidade --')
    while True:
        q = lerInteiro()
        if q > 0:
            return q
        else:
            print('Erro - a quantidade deve ser positiva.')

### Função de cadastro Valor ##################################################################
def validaCadastroValor():
    print()
    print('-- Valor --')
    v = lerInteiro()
    if v > 0:
        return v
    else:
        print('Erro - o valor deve ser positiva.')

### Função de cadastro Cor ##################################################################
def validaCadastroCor():
    print()
    print('-- Cor --')
    mostraListaExemplo(listaCorExemplo)
    while True:
        try:
            escolha = lerInteiro()
            if listaCorExemplo[escolha] in listaCorExemplo:
                c = listaCorExemplo[escolha]
                return c
        except:
            print('Item inexistente digite o numero do item acima.')

### Função para mostrar mensagem formatada ##################################################################
def menuEscolha(mensagem):
    print('-'*60)
    print('-'*5+mensagem+'-'*5)
    print('-'*60)