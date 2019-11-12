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
    else:
        print()
        validacao.menuEscolha(' Lista vazia! ')
