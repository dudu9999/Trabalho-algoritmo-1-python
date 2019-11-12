import validacao

def cadastrarCores(listaProdutos):
    while True:
        validacao.mostraListaExemplo(validacao.listaCorExemplo)
        print('\n----- Cor -----')
        cor  = input('Digite a Cor que deseja cadastrar: ')
        if len(cor) == 0 or len(cor)> 20:
            print('Cor não digitada ou muito grande')
        else:
            validacao.listaCorExemplo.append(cor)
            print()
            print('-' * 60)
            print('-' * 5 + ' LISTA ATUALIZADA ' + '-' * 5)
            validacao.mostraListaExemplo(validacao.listaCorExemplo)
            print('-' * 60)
            print()
            break