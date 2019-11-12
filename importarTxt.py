### Função que pega os dados de um txt e coloca na lista ###########################################################
import os

import tenis
import validacao
from produto import Produto


def ImportarTxt(listaProdutos):

    fileName = input('\nQual o nome do banco de dados deseja importar?\nOu tecle [ENTER] para usar a padrão ')

    if (len(fileName) > 0):
        fileName = fileName + '.txt'
    else:
        fileName = 'dados.txt'

    if (len(fileName) > 0):
        try:
            dados = open(fileName, 'r')
        except FileNotFoundError:
            return print('\nEsse banco de dados não existe ainda\nCopie uma banco de daos para a pasta\nOu crei um novo!!')
    else:
        if os.path.isfile('dados.txt'):
            dados = open('dados.txt', 'r')
        else:
            print('\nEsse banco de dados não existe ainda\nCopie uma banco de daos para a pasta\nOu crei um novo!!')
            ImportarTxt(listaProdutos)
    x = 0
    # Efetua a leitura das linhas do arquivo
    for line in dados.readlines():
        # Quebra a linha lida em uma lista, a cada espaço encontrado é gerado um item na lista
        sapato_item = line.strip().split(' ')

        t = tenis.Tenis()
        t.set_modelo(str(sapato_item[0]))
        t.set_numeracao(str(sapato_item[1]))
        t.set_cor(str(sapato_item[2]))

        prod = Produto()
        prod.set_quantidade(str(sapato_item[3]))
        prod.set_valor(str(sapato_item[4]))
        prod.set_tenis(t)

        listaProdutos.append(prod)
        x+=1

    validacao.menuEscolha(' Importado do TXT com sucesso! ')
    dados.close()
