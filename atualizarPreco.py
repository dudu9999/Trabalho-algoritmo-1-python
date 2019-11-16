# Trabalho - Utilizando Listas
# Autor:  Eduardo Caetano

import validacao
import relatorio

#############################################################
def atulizaPreco(listaProdutos):
    if len(listaProdutos) != 0:
        relatorio.relatorioGeral(listaProdutos)
        while True:
            print()
            print('Escolha um item que deseja atualizar o preco.')
            escolha = validacao.lerInteiro()

            if escolha > (len(listaProdutos) - 1) or escolha < 0:
                print('-'*60)
                print('-'*30+' Item escolhido fora da lista! '+'-'*30)
                print('-'*30+'  digite o numero de um iten  que esteja na  lista! '+'-'*30)
                print('-' * 60)
            else:
                print()
                print('Qual o valor atualizado que deseja inserir')
                precoAtual = validacao.lerInteiro()
                if precoAtual <= 0 or precoAtual > 10000:
                    print()
                    print('Esse preco é muito elevado ou valor digitado esta errado!')
                else:
                    listaProdutos[escolha].set_valor(precoAtual)
                    validacao.menuEscolha(' Preço atualizado com sucesso ')

                    print()
                    print('-' * 50)
                    print('-' * 5 + ' LISTA ATUALIZADA ' + '-' * 5)
                    relatorio.relatorioGeral(listaProdutos)
                    break
    else:
        print()
        validacao.menuEscolha(' Lista vazia! ')