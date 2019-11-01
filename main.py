###### variaveis e listas  ###################################################################
# Imports
import os
import sys
import struct
import Cadastro
import CadastroCor
import AtualizarPreco
import ExportarTxt
import ImportarTxt
import Relatorio
import Vender
import Validacao

### Listas vazias
listaTenis = []

# Listas com dados

# listas de exemplo
listaModeloExemplo = ('Tradicional', 'Esportivo', 'Caminhada', 'Corrida')
listaCorExemplo = ['Branco', 'Azul', 'Amarelo', 'Vermelho']


# Variaveis

### Criação da Classe Tenis ###############################################
class Tenis:
    def __init__(self, modelo, numeração, quantidade, valor, cor):
        self.__modelo = modelo
        self.__numeração = numeração
        self.__quantidade = quantidade
        self.__valor = valor
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


###  Execução ######################################################################
###  Execução ######################################################################
while True:
    escolha = Validacao.lerInteiro(menu())

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
        Cadastro.cadastroTotal()

#        try:
#            Cadastro.cadastroTotal()
#        except AttributeError:
#            print("Não deu mermão!")
#            raise Cadastro.cadastroTotal()


    elif escolha == 2:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 2 - Relatorio ----------')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        Relatorio.relatorioGeral()

    elif escolha == 3:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 3 - Realizar Venda -----')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        # realizarVenda(sapataria)

    elif escolha == 4:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 4 - Atualizar preços -----')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        # atulizaPreco(sapataria)

    elif escolha == 5:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar Cores -----')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        # cadastrarCores(listaCorExemplo)

    elif escolha == 6:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar no TXT -----')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        # guardaTxt(sapataria)

    elif escolha == 7:
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Recuperar no TXT -----')
        print(
            '----------------------------------------------------------------------------------------------------------------------------------')
        # recuperaTxt(sapataria)

    else:
        print('Item do menu inexistente')

##########  Daqui pra baixo não ha mais nada! #######################################################
##########  Daqui pra baixo não ha mais nada! #######################################################
##########  Daqui pra baixo não ha mais nada! #######################################################



















