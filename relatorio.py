# Trabalho - Utilizando Listas
# Autor:  Eduardo Caetano

import validacao

def relatorioGeral(listaProdutos):
    x = 0
    if len(listaProdutos) != 0:
        print('Item    Modelo     Numeração     Cor      Quantidade    Valor  ')
        for t in listaProdutos:
            print(' ' + str(x).ljust(3, ' ') + '  ' +
                  str(t.get_tenis().get_modelo()).center(11, ' ') +
                  str(t.get_tenis().get_numeracao()).center(13, ' ') +
                  str(t.get_tenis().get_cor()).center(10, ' ') +
                  str(t.get_quantidade()).center(13, ' ') +
                  str(t.get_valor()).center(10, ' '))
            x+=1
        print('-'*60)
        print(' '*10+'Total em Estoque R$:', totalEstoque(listaProdutos))
        print('O tenis de ID:', possuiMais(listaProdutos), ' é o que possui ', round(calculaPrecent(listaProdutos)),
              '% de todo o estoque!')
        print('-'*60)
    else:
        print()
        validacao.menuEscolha(' Lista vazia! ')

### Função que calcula o total #############################################################
def totalEstoque(listaProdutos):
    somaTotal = 0
    ind = 0
    for x in listaProdutos:
        somaTotal = somaTotal + (int(listaProdutos[ind].get_valor()) * int(listaProdutos[ind].get_quantidade()))
        ind += 1
    return somaTotal

### Função para calcular o percentual #######################################################
def calculaPrecent(listaProdutos):
    per = 0
    ind = 0
    for x in listaProdutos:
        per = per + int(listaProdutos[ind].get_quantidade())
        ind+=1
    per = ((100*(int(listaProdutos[possuiMais(listaProdutos)].get_quantidade())) / per))
    return per

### Função para mostrar qual tenis possui mais em estoque ######################################
def possuiMais(listaProdutos):
    ind = 0
    val_Atual = 0
    indMaior = 0
    for x in listaProdutos:
        if int(listaProdutos[ind].get_quantidade()) > int(val_Atual):
            val_Atual = listaProdutos[ind].get_quantidade()
            indMaior = ind
        ind+=1
    return indMaior # valor do indice do que possui mais no estoque