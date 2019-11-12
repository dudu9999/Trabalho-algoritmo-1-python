###### variaveis e listas  ###################################################################
# Imports
import sys
import struct

import relatorio
import tenis
from produto import Produto
import cadastroCor
import atualizarPreco
import exportarTxt
import importarTxt
import vender
import validacao

### Listas vazias
listaProdutos = []

### Variaveis
x = 0
espaco = 5

####################################################################################
###  Execução ######################################################################
####################################################################################
while True:
    validacao.menu()
    escolha = validacao.lerInteiro()

    if escolha == 0:
        validacao.menuEscolha(' Ate logo amigo! ')
        sys.exit()

    elif escolha == 1:
        validacao.menuEscolha(' Opcao 1 - Cadastro ')
        t = tenis.Tenis()
        t.set_modelo(validacao.validaCadastroModelo())
        t.set_numeracao(validacao.validaCadastroNumeracao())
        t.set_cor(validacao.validaCadastroCor())

        prod = Produto()
        prod.set_quantidade(validacao.validaCadastroQuantidade())
        prod.set_valor(validacao.validaCadastroValor())
        prod.set_tenis(t)

        listaProdutos.append(prod)

    elif escolha == 2:
        validacao.menuEscolha(' Opcao 2 - Relatorio ')
        relatorio.relatorioGeral(listaProdutos)

    elif escolha == 3:
        validacao.menuEscolha(' Opcao 3 - Realizar Venda ')
        vender.realizarVenda(listaProdutos)

    elif escolha == 4:
        validacao.menuEscolha(' Opcao 4 - Atualizar preços ')
        atualizarPreco.atulizaPreco(listaProdutos)

    elif escolha == 5:
        validacao.menuEscolha(' Opcao 5 - Cadastrar Cores ')
        cadastroCor.cadastrarCores(validacao.listaCorExemplo)

    elif escolha == 6:
        validacao.menuEscolha(' Opcao 5 - Cadastrar no TXT ')
        exportarTxt.ExportarTxt(listaProdutos)

    elif escolha == 7:
        validacao.menuEscolha(' Opcao 5 - Recuperar no TXT ')
        # recuperaTxt()

    else:
        print('Item do menu inexistente')

##########  Daqui pra baixo não ha mais nada! #######################################################
#####################################################################################################
#####################################################################################################