# Trabalho - Utilizando Listas
# Autor:  Eduardo Caetano

'''
Descrição do trabalho:
Utilizando o menu abaixo, desenvolva um programa que controle o estoque
da famosa loja Tenis do Tio Ivo. A loja é especializada em venda de tenis.
Utilizando estrutura de listas você deverá armazenar os seguintes dados:
    Modelo     , Cor     , Numeração     , Quantidade e ValorUnitario
    lstModelo[], lstCor[], lstNumeracao[], lstQtd[]   e lstValorUnit[]


Detalhamento:
Na opção 1, você deverá cadastrar o modelo do tenis, a numeração, a quantidade de pares,
            o valor a ser vendido e, a cor.
            O modelo deverá ser um dos seguintes: Tradicional, Esportivo, Caminhada, Corrida.
            A numeração deverá ser um valor entre 22 e 46.
            A quantidade deverá sempre ser acrescida ao estoque. (Não aceitar qt negativa)
            O valor deve ser maior que zero.
            A cor deverá ser uma das cores cadastradas anteriormente.

Na opção 2, você deverá listar dos dados em estoque. mostrando o valor total
            exemplo:
            Modelo       Numeração  Quant.   Valor      Cor
            Esportivo      23         5       120.00    Branca
            Corrida        37         7        99,80    Azul
            ...
            -----------------------------------------------------
            Total em Estoque R$:  1298.60
            ...

Na opção 3, você deverá realizar uma venda.
            Localize o produto, veja se existem quantidades suficientes em estoque,
            mostre o valor total da venda e, ao confirmar dê baixa no estoque.
            Exemplo:
                Produto: Corrida, 37, Azul
                Quantidade: 1
                Preço Total: 99,80

Na opção 4, você deverá localizar um produto e atualizar seu preço.
            Exemplo:
                Produto: Tradicional
                Quantidade: 8   Cor: Branca   (informar esses dados)
                Novo Preço: 110.00            (digitar)

Na opção 5, você deverá cadastrar as cores para poder escolher na hora de
            cadastrar o estoque.
'''