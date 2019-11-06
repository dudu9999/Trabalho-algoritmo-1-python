###### variaveis e listas  ###################################################################
# Imports
import os
import sys
# import struct

import tenis
from cadastro import Cadastro
from cadastroCor import CadastroCor
from atualizarPreco import AtualizarPreco
from exportarTxt import ExportarTxt
from importarTxt import ImportarTxt
from relatorio import Relatorio
from vender import Vender
from validacao import Validacao

### Listas vazias
listaTenis = []

# Listas com dados

# listas de exemplo
listaModeloExemplo = ('Tradicional', 'Esportivo', 'Caminhada', 'Corrida')
listaCorExemplo = ['Branco', 'Azul', 'Amarelo', 'Vermelho']


# Variaveis

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
    7-  Recupera do TXT
    Escolha: '''
    return menu

### mostra a lista de exemplo ##############################################################
def mostraListaExemplo(listaExemplo):
    ind = 0
    for x in listaExemplo:
        print('  ' + str(ind) + ' - ' + listaExemplo[ind])
        ind += 1
    print('')
############################################################################################
self.__quantidade = quantidade
self.__valor = valor
############################################################################################

############################################################################################




###  Execução ######################################################################
###  Execução ######################################################################
while True:
    menu()
    escolha = validacao.Validacao.lerInteiro('Mensagem')

    if escolha == 0:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('____________ FIM _____________\n_______ Ate logo amigo! _______')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        sys.exit()
        break

    elif escolha == 1:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 1 - Cadastro -----------')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        cadastro.Cadastro.cadastroTotal()

#        try:
#            Cadastro.cadastroTotal()
#        except AttributeError:
#            print("Não deu mermão!")
#            raise Cadastro.cadastroTotal()


    elif escolha == 2:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 2 - Relatorio ----------')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        #relatorio.relatorioGeral()

    elif escolha == 3:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 3 - Realizar Venda -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # realizarVenda(sapataria)

    elif escolha == 4:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 4 - Atualizar preços -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # atulizaPreco(sapataria)

    elif escolha == 5:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar Cores -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # cadastrarCores(listaCorExemplo)

    elif escolha == 6:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar no TXT -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # guardaTxt(sapataria)

    elif escolha == 7:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Recuperar no TXT -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # recuperaTxt(sapataria)

    else:
        print('Item do menu inexistente')

##########  Daqui pra baixo não ha mais nada! #######################################################
##########  Daqui pra baixo não ha mais nada! #######################################################
##########  Daqui pra baixo não ha mais nada! #######################################################



















