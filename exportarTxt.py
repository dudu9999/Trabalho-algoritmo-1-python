####Função que armazena o conteudo da lista em um arquivo TXT ########################
import os
import validacao

def ExportarTxt(listaProdutos):
    if (len(listaProdutos) != 0):
        fileName = input('\nQual o nome do banco de dados deseja exportar?\nOu tecle [ENTER] para usar a padrão ')

        if (len(fileName) > 0):
            fileName = fileName + '.txt'
        else:
            fileName = 'dados.txt'

        if (fileName != 'dados.txt'):
            file1 = open(fileName, 'w')
        else:
            if os.path.isfile('dados.txt'):
                file1 = open('dados.txt', 'r')
            else:
                print('\nEsse banco de dados não existe ainda\nCopie uma banco de daos para a pasta\nOu crei um novo!!')
                ExportarTxt(listaProdutos)

        for x in range(len(listaProdutos)):
            file1.write(
                    str(listaProdutos[x].get_tenis().get_modelo())    + ' ' +
                    str(listaProdutos[x].get_tenis().get_numeracao())  + ' ' +
                    str(listaProdutos[x].get_tenis().get_cor())        + ' ' +
                    str(listaProdutos[x].get_quantidade())             + ' ' +
                    str(listaProdutos[x].get_valor())                  + '\n'
            )

        file1.close()
        validacao.menuEscolha(' Armazenado no TXT sucesso! ')

    else:
        print('\nNão existe item nas listas para armazenar no txt!\n')
