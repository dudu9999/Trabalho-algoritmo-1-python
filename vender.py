# Trabalho - Utilizando Listas
# Autor:  Eduardo Caetano

### Realizar Venda ##############################################################################
import validacao
import relatorio


def realizarVenda(listaProdutos):

    if len(listaProdutos) != 0:
        relatorio.relatorioGeral(listaProdutos)
        while True:
            print()
            print('Escolha um para vender: ')
            escolha = validacao.lerInteiro()
            if escolha > (len(listaProdutos) - 1) or escolha < 0:
                print('Item escolhido fora da lista!\n digite o numero de um iten  que esteja na  lista!')
            else:
                print()
                print('Quantos voce deseja vender: ')
                quntidadeVenda = validacao.lerInteiro() # t.get_quantidade()
                if quntidadeVenda > int(listaProdutos[escolha].get_quantidade()) or quntidadeVenda <= 0:
                    print('Voce nao tem essa quantidade ou valor digitado esta errado!')
                else:
                    listaProdutos[escolha].set_quantidade(listaProdutos[escolha].get_quantidade() - quntidadeVenda)
                    if int(listaProdutos[escolha].get_quantidade()) == 0:
                        limpaItem(listaProdutos, escolha)

                    validacao.menuEscolha(' Venda realisada com sucesso ')

                    print()
                    print('-'*60)
                    print('-'*5+' LISTA ATUALIZADA '+'-'*5)
                    relatorio.relatorioGeral(listaProdutos)
                    print('-'*60)
                    break
    else:
        print()
        validacao.menuEscolha(' Lista vazia! ')

def limpaItem(listaProdutos, escolha):
    listaProdutos.pop(escolha)
