# Trabalho 01 - Utilizando Listas
# Autor:  Eduardo Caetano
# atualizar preço por modelo
# se ja houver no dicionario

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
                Quantidade: 8   Cor: Branca   (informar e {Esportivo      23         5 }sses dados)
                Novo Preço: 110.00            (digitar)

Na opção 5, você deverá cadastrar as cores para poder escolher na hora de 
            cadastrar o estoque.

            dados_dic = {}


            a = input()

            chave = (a + ' '+ b +' '+ c)

             preco = input()
            quant = input()

            

            lista_dados =[]

            lista_dados.append(preco )
            lista_dados.append(quant )
            
    
            dados = {chave : lista_dados}            

           
            dados_dic.apend(dados)

            [{'Esportivo - 23 - preto' : [120.00   , 5]}]


            
'''

###### variaveis e listas  ###################################################################
# Imports
import os
import sys
import struct

### Listas vazias 
sapataria = list()

### Listas com dados
##sapataria = [{'Modelo': 'Caminhada', 'Numeração': 40, 'Quantidade': 100, 'Valor': 1000, 'Cor': 'Vermelho'},
##                    {'Modelo': 'Esportivo', 'Numeração': 42, 'Quantidade': 50, 'Valor': 300, 'Cor': 'Amarelo'},
##                    {'Modelo': 'Corrida', 'Numeração': 44, 'Quantidade': 20, 'Valor': 150, 'Cor': 'Branco'},
##                    {'Modelo': 'Tradicional', 'Numeração': 44, 'Quantidade': 20, 'Valor': 150, 'Cor': 'Branco'}]

# listas de exemplo
listaModeloExemplo = ('Tradicional','Esportivo','Caminhada','Corrida')
listaCorExemplo = ['Branco','Azul','Amarelo','Vermelho']

# Variaveis
sapato = dict()
depoisDeAdicionadoNoEstoque = False
jaExiste = False


def menu():
    menu ='''
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

### Função para ler um inteiro ##############################################################
def lerInteiro(mens): 
    while True:
        try:
            n = int(input(mens))            
            return n
        except:
            input('...Erro. Você não digitou um número inteiro.')

### Função para mostrar a lista ou seja relatorio ( Opção 2 ) ####################################################
def mostraLista(sapataria):
    espaco = '  '
    x = 0
    ind = 0
    print('Item    Modelo       Numeração  Quantidade       Valor             Cor')
    for x in range(len(sapataria)):

        if sapataria[x]['Modelo'] == 'Tradicional':
            # Tradicional
            espaco = 18
            espaco2 = 20
            
        if sapataria[x]['Modelo'] == 'Esportivo':
            # Esportivo
            espaco = 19
            espaco2 = 20
            
        if sapataria[x]['Modelo'] == 'Corrida':
            # Corrida
            espaco = 20
            espaco2 = 20
            
        if sapataria[x]['Modelo'] == 'Caminhada':
            # Caminhada
            espaco = 15
            espaco2 = 19

        print('   '+str(x).ljust(7,' ')+sapataria[x]['Modelo'].ljust(espaco,' ')+str(sapataria[x]['Numeração']).ljust(espaco2,' ')+
                    str(sapataria[x]['Quantidade']).ljust(espaco2,' ')+str(sapataria[x]['Valor']).ljust(15,' ')+sapataria[x]['Cor'].ljust(15,' '))
        
### mostra a lista de exemplo ##############################################################
def mostraListaExemplo(listaExemplo):
    ind = 0
    for x in listaExemplo:
        print('  '+str(ind)+' - '+listaExemplo[ind])
        ind += 1
    print('')

### Funcção que efetua o cadastro  ######################################################### 
def cadastroTotal():
    resposta = 'S'
    jaExiste
    
    cadastroModelo(sapataria)
    if jaExiste == False:
        cadastroNumeracao(sapataria)
        cadastroQuantidade(sapataria)
        cadastroValor(sapataria)
        cadastroCor(sapataria)
        sapataria.append(sapato.copy())
        
    print('----------------------------------------------------------------------------------------------------------------------------')
    resposta = str(input(' [ s = SIM // n = NÃO ]\nDeseja verificar outro: '))

    if(resposta.upper() == 'N' ):
        print()
        print('---------------------------------- LISTA ATUALIZADA --------------------------------------------------------')
        mostraLista(sapataria)
        
        
### Função que cadastra o modelo na lista #########################################################################
def cadastroModelo(sapataria):
    global jaExiste
    jaExiste = False
    while(True):
        while(True):
            if(jaExiste == False):
                print('\n-------- Modelo --------')
                mostraListaExemplo(listaModeloExemplo)
                modelo  = lerInteiro('Digite o numero do modelo do tenis\nda lista que deseja adicionar: ')
                if(modelo >= 0 and modelo <= 3):
                    for x in range(len(sapataria)):
                        print('x: ',x,' sapataria[x][Modelo]: ',sapataria[x]['Modelo'])
                        
                        if listaModeloExemplo[modelo] == sapataria[x]['Modelo']:
                            jaExiste = True
                            print(' ------------------------------------------------------------------------')
                            print('----------------- Esse modelo ja existe! ------------------')
                            print(' Você deseja adicionar mais no desse modelo')
                            print(' no estoque ou quer adicionar outro novo?')
                            print(' ------------------------------------------------------------------------')
                            print(' [  1 - Novo  ou  2 - Adicionar mais estoque  ] ')

                            escolhaEstoque = lerInteiro(' ')
                            if escolhaEstoque == 2:
                                adicionarMaisQuantidade(sapataria, modelo, x)
                                jaExiste = True
                                break
                            if escolhaEstoque == 1:
                                sapato['Modelo'] = str(listaModeloExemplo[modelo])
                                break
                            break
                        
                else:
                    print('\n----------------------------------------------------------------------------------------------------------------------------')
                    print('---------------------------------------------    Erro!  -----------------------------------------------------------------')
                    print('---------------------------------- Numero digitado errado! -------------------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------------------\n')

            break
        break
    
### Função que cadastra a numeração na lista #######################################################################
def cadastroNumeracao(sapataria):
        if depoisDeAdicionadoNoEstoque == True:
            print('')
        else:
            # valida numeração
            while True:
                print('\n--------------------- Numeracao -------------------------')
                numeracao = lerInteiro('Digite a numeracao do tenis [ 22 - 46]: ') 
                if numeracao >= 22 and numeracao <= 46 :
                    sapato['Numeração'] = numeracao
                    break
                else:
                    print('\n----------------------------------------------------------------------------------------------------------------------------')
                    print('---------------------------------------------    Erro!  -----------------------------------------------------------------')
                    print('---------------------- digite um numero no intervalo de 22 ate 48 -------------------------------')
                    print('--------------------------- Digite novamento um Numero! ----------------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------------------\n')

        
### Função que cadastra a quantidade na lista #######################################################################
def cadastroQuantidade(sapataria):
        if depoisDeAdicionadoNoEstoque == True:
            print('')
        else:
            # valida Quantidade
            while True:
                print('\n--------------------- Quantidade -------------------------')                
                quantidade = lerInteiro('Digite a quantidade de tenis: ') 
                if quantidade == 0 or quantidade < 0 or quantidade > 500:
                    print('\n----------------------------------------------------------------------------------------------------------------------------')
                    print('---------------------------------------------    Erro!  -----------------------------------------------------------------')
                    print('---------------------- Quantidade muito alta ou muito baixa ----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------------------\n')
                else:
                    sapato['Quantidade'] = quantidade 
                    break
            
        
### Função que cadastra o valor na lista #######################################################################
def cadastroValor(sapataria):
        if depoisDeAdicionadoNoEstoque == True:
            print('')
        else:
            # valida Valor
            while True:
                print('\n------------------------- Valor ------------------------------')
                valor = lerInteiro('Digite o valor do tenis: ') 
                if valor <= 10 or valor > 5000:
                    print('\n----------------------------------------------------------------------------------------------------------------------------')
                    print('---------------------------------------------    Erro!  -----------------------------------------------------------------')
                    print('------------------------ Valor não digitado ou muito grande -----------------------------------------')
                    print('----------------------------------------------------------------------------------------------------------------------------\n')
                    
                else:
                    sapato['Valor'] = valor
                    break  

### Função que cadastra a cor na lista #######################################################################
def cadastroCor(sapataria):
        print()
        while(True):
            print('\n--------------------------- Cor -------------------------------')
            mostraListaExemplo(listaCorExemplo)
            cor  = lerInteiro('Digite o numero da cor do tenis\nda lista que deseja adicionar: ')        
            if(cor >= 0 and cor < len(listaCorExemplo)):
                sapato['Cor'] = str(listaCorExemplo[cor])
                break
            else:
                print('\n----------------------------------------------------------------------------------------------------------------------------')
                print('---------------------------------------------    Erro!  -----------------------------------------------------------------')
                print('---------------------------------- Numero digitado errado! -------------------------------------------------')
                print('----------------------------------------------------------------------------------------------------------------------------\n')
        print('----------------------------------------------------------------')

### Relatorio ( Opção 3 )##############################################################################
def relatorioGeral(sapataria):
    if len(sapataria) != 0:
        mostraLista(sapataria)
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('          Total em Estoque R$:',total(sapataria))
        print('O tenis de ID:',possuiMais(sapataria),' é o que possui ',round(calculaPrecent(sapataria)),'% de todo o estoque!')
        print('E só o tenis de ID:',possuiMais(sapataria),' que esta parado, possui o valor de  R$',int(sapataria[possuiMais(sapataria)]['Quantidade'])*int(sapataria[possuiMais(sapataria)]['Valor']),' de prejuizo!')
        print('----------------------------------------------------------------------------------------------------------------------------------\n')
    else:
        print('\nLista vazia!')

### Função que calcula o total #############################################################
def total(sapataria):
    somaTotal = 0
    ind = 0
    for x in sapataria:
        somaTotal = somaTotal + ( int(sapataria[ind]['Valor']) * int(sapataria[ind]['Quantidade'] ))
        ind+=1
    return somaTotal

### Função para calcular o percentual #######################################################
def calculaPrecent(sapataria):
    per = 0
    ind = 0
    for x in sapataria:
        per = per + sapataria[ind]['Quantidade'] 
        ind+=1
    per = (100*(sapataria[possuiMais(sapataria)
                          ]['Quantidade'] / per))
    return per

### Função para mostrar qual tenis possui mais em estoque ######################################
def possuiMais(sapataria):
    ind = 0
    val_Atual = 0
    indMaior = 0
    for x in sapataria:
        if sapataria[ind]['Quantidade'] > val_Atual:
            val_Atual = sapataria[ind]['Quantidade']
            indMaior = ind
        ind+=1
    return indMaior # valor do indice do que possui mais no estoque

### Realizar Venda ##############################################################################
def realizarVenda(sapataria):
    if len(sapataria) != 0:
        mostraLista(sapataria)
        while True:
            print()
            escolha  = lerInteiro('Escolha um para vender: ')
            if escolha > (len(sapataria)-1) or escolha < 0:
                    print('Item escolhido fora da lista!\n digite o numero de um iten  que esteja na  lista!')
            else:
                print()
                quntidadeVenda  = lerInteiro('Quantos voce deseja vender: ')
                if quntidadeVenda > sapataria[escolha]['Quantidade'] or quntidadeVenda <= 0:
                        print('Voce nao tem essa quantidade ou valor digitado esta errado!')
                else:
                    sapataria[escolha]['Quantidade'] = sapataria[escolha]['Quantidade'] - quntidadeVenda
                    if sapataria[escolha]['Quantidade'] == 0:
                        limpaItem(sapataria, escolha)

                    print('\n---------------------------------------------------------------------------------------------------------------------------')
                    print('--------------------------- Venda realisada com sucesso -----------------------------------------------')
                    print('---------------------------------------------------------------------------------------------------------------------------\n')
                    
                    print('---------------------------------- LISTA ATUALIZADA --------------------------------------------------------')
                    mostraLista(sapataria)
                    print('---------------------------------------------------------------------------------------------------------------------------')

                    break
        else:
            print('\nLista vazia!')

### Função que se nao houver nenhum tenis no estoque entao remove o tenis #######################
def limpaItem(sapataria, escolha):
    sapataria.pop(escolha)

### Função para atualizar o preço (Opção 4) ################################################
def atulizaPreco(sapataria):        
        if len(sapataria) != 0:
            mostraLista(sapataria)
            while True:
                print()
                escolha  = lerInteiro('Digite o numero de um item que deseja atualizar o preco:  ')

                if escolha > (len(sapataria)-1) or escolha < 0:
                    print('---------------------------------------------------------------------------------------------------------------------------')
                    print('--------------------------- Item escolhido fora da lista! --------------------------------------------------')
                    print('--------------- digite o numero de um iten  que esteja na  lista! ------------------------------')
                    print('---------------------------------------------------------------------------------------------------------------------------\n')
                else:
                    print()
                    precoAtual  = lerInteiro('Qual o valor atualizado que deseja inserir:  ')
                    if precoAtual <= 0 or precoAtual > 10000:
                        print()
                        print('Esse preco é muito elevado ou valor digitado esta errado!')
                    else:
                        sapataria[escolha]['Valor'] = precoAtual
                        print('\n---------------------------------------------------------------------------------------------------------------------------')
                        print('--------------------------- Preço atualizado com sucesso ----------------------------------------------')
                        print('---------------------------------------------------------------------------------------------------------------------------\n')
                        
                        print('---------------------------------- LISTA ATUALIZADA --------------------------------------------------------')
                        mostraLista(sapataria)
                        break
        else:
            print('\nLista vazia!')

### Função para cadastrar cores ( Opção 5 ) ###############################################
def cadastrarCores(listaCorExemplo):
    while True:
        #mostraListaExemplo(lstCor)
        print('\n----- Cor -----')
        cor  = input('Digite a Cor que deseja cadastrar: ')
        if len(cor) == 0 or len(cor)> 20:
            print('Cor não digitada ou muito grande')
        else:
            listaCorExemplo.append(cor)
            print('\n---------------------------------- LISTA ATUALIZADA --------------------------------------------------------')
            mostraListaExemplo(listaCorExemplo)
            break

### Função para adicionara mais sapatos no estoque se caso já existir ##################
def adicionarMaisQuantidade(sapataria, modelo, x):
    while True:
        
        quantidadeAdd = lerInteiro('\nQuanto deseja adicionar: ')
        if quantidadeAdd <= 0 and quantidadeAdd>500:
            print('Numero deve ser maior que 0 (Zero) e menor que 500 (Quientos)')
        else:
            sapataria[x]['Quantidade'] = (quantidadeAdd + sapataria[x]['Quantidade'])
            break
        
####Função que armazena o conteudo da lista em um arquivo TXT ########################
def guardaTxt(sapataria):
    if(len(sapataria) != 0):
        fileName = input('\nQual o nome do banco de dados deseja exportar?\nOu tecle [ENTER] para usar a padrão ')

        if(len(fileName) > 0):
            fileName = fileName + '.txt'
        else:
            fileName = 'dados.txt'
        
        

        if(fileName != 'dados.txt'):
            file1 = open(fileName,'w')
        else:
            if os.path.isfile('dados.txt'):
                file1 = open('dados.txt', 'r')
            else:
                print('\nEsse banco de dados não existe ainda\nCopie uma banco de daos para a pasta\nOu crei um novo!!')
                guardaTxt(sapataria)
            
        ind = 0    

        for x in range(len(sapataria)):
            file1.write(sapataria[x]['Modelo']+' '+str(sapataria[x]['Numeração'])+' '+str(sapataria[x]['Quantidade'])+' '+str(sapataria[x]['Valor'])+' '+sapataria[x]['Cor']+'\n')
    
            ind += 1

        file1.close()
        print('\n---------------------------------------------------------------------------------------------------------------------------')
        print('--------------------------- Armazenado no TXT sucesso! -----------------------------------------------')
        print('---------------------------------------------------------------------------------------------------------------------------\n')
    
    else:
        print('\nNão existe item nas listas para armazenar no txt!\n')

### Função que pega os dados de um txt e coloca na lista ###########################################################
def recuperaTxt(sapataria):
    sapato = dict()
    fileName = input('\nQual o nome do banco de dados deseja importar?\nOu tecle [ENTER] para usar a padrão ')

    if(len(fileName) > 0):
        fileName = fileName + '.txt'
    else:
        fileName = 'dados.txt'

    if(len(fileName) > 0):
        dados = open(fileName,'r')
    else:
        if os.path.isfile('dados.txt'):
            dados = open('dados.txt', 'r')
        else:
            print('\nEsse banco de dados não existe ainda\nCopie uma banco de daos para a pasta\nOu crei um novo!!')
            recuperaTxt(sapataria)

    #Efetua a leitura das linhas do arquivo
    for line in dados.readlines():
        #Quebra a linha lida em uma lista, a cada espaço encontrado é gerado um item na lista
        sapato_item = line.strip().split(' ')
        
        sapato['Modelo']        = str(sapato_item[0])
        sapato['Numeração'] = int(sapato_item[1])
        sapato['Quantidade'] = int(sapato_item[2])
        sapato['Valor']           = str(sapato_item[3])
        sapato['Cor']              = str(sapato_item[4])

        sapataria.append(sapato.copy())

    print('\n---------------------------------------------------------------------------------------------------------------------------')
    print('--------------------------- Importado do TXT com sucesso! --------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------------------------\n')
    dados.close()


       
###  Execução ######################################################################
while True:
    escolha = lerInteiro(menu())

    if escolha == 0:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('____________ FIM _____________\n_______ Ate logo amigo! _______')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        sys.exit()
        break
    
    elif escolha == 1:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 1 - Cadastro -----------')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        cadastroTotal()
        
    elif escolha == 2:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 2 - Relatorio ----------')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        relatorioGeral(sapataria)
        
    elif escolha == 3:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 3 - Realizar Venda -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        realizarVenda(sapataria)
        
    elif escolha == 4:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 4 - Atualizar preços -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        atulizaPreco(sapataria)
        
    elif escolha == 5:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar Cores -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        cadastrarCores(listaCorExemplo)

    elif escolha == 6:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Cadastrar no TXT -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        guardaTxt(sapataria)

    elif escolha == 7:
        print('\n----------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 5 - Recuperar no TXT -----')
        print('----------------------------------------------------------------------------------------------------------------------------------')
        recuperaTxt(sapataria)

    else:
        print('Item do menu inexistente')

##########  Daqui pra baixo não ha mais nada! #######################################################






























