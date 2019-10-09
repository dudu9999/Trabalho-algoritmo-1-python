# Trabalho 01 - Utilizando Listas
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

###### variaveis e listas  ###################################################################
# Imports
import os

### Listas com dados
#lstModelo, lstCor = ['Tradicional','Esportivo','Caminhada','Corrida'],['Branco','Azul','Amarelo','Vermelho']
#lstNumeracao, lstQtd, lstValorUnit = [42,40,45,39],[20,10,25,15],[500,200,600,400]

### Listas vazias 
lstModelo, lstCor = [],[]
lstNumeracao, lstQtd, lstValorUnit = [],[],[]

# listas de exemplo
modeloExemplo = ('Tradicional','Esportivo','Caminhada','Corrida')
listaCorExemplo = ['Branco','Preto','Azul','Amarelo','Vermelho','Verde','Rosa','Roxo']

# Variaveis
escolha, quntidadeVenda, precoAtual, numeracao, valor, quantidade = 0, 0, 0, 0, 0, 0
modelo, cor, resposta = '','',''
depoisDeAdicionadoNoEstoque = False
### Função para ler um inteiro ##############################################################
def lerInteiro(mens): 
    while True:
        try:
            n = int(input(mens))            
            return n
        except:
            input('...Erro. Você não digitou um número inteiro.')
### Função para mostrar a lista (Relatorio) ####################################################
            
def mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit):
    espaco2 = 0
    ind = 0
    print('Indice      Modelo           Numeração  Quantidade       Valor           Cor')
    for x in range(len(lstModelo)):
        if lstModelo[x] == 'Tradicional':
            # Tradicional
            espaco = 14
            espaco2 = 20
            
        if lstModelo[x] == 'Esportivo':
            # Esportivo
            espaco = 14
            espaco2 = 20
            
        if lstModelo[x] == 'Corrida':
            # Corrida
            espaco = 16
            espaco2 = 20
            
        if lstModelo[x] == 'Caminhada':
            # Caminhada
            espaco = 10
            espaco2 = 22
        
        print(' '+str(ind).center(5,' ')+ \
              lstModelo[x].center(23,' ')+ \
              str(lstNumeracao[x]).center(espaco,' ')+ \
              str(lstQtd[x]).center(espaco2,' ')+ \
              str(lstValorUnit[x]).center(15,' ')+ \
              lstCor[x].center(15,' '))
        ind += 1
    print('')

### mostra a lista de exemplo ##############################################################
def mostraListaExemplo(listaCorExemplo):
    ind = 0
    for x in listaCorExemplo:
        print('  '+str(ind)+' - '+listaCorExemplo[ind])
        ind += 1
    print('')
### Função que se nao houver nenhum tenis no estoque entao remove o tenis #######################
def limpaItem(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit,escolha):
    lstQtd.pop(escolha)
    lstModelo.pop(escolha)
    lstCor.pop(escolha)
    lstNumeracao.pop(escolha)
    lstValorUnit.pop(escolha)
### Função que calcula o total #############################################################
def total(lstQtd,lstValorUnit):
    somaTotal = 0
    ind = 0
    for x in lstQtd:
        somaTotal = somaTotal + ( lstQtd[ind] * lstValorUnit[ind] )
        ind+=1
    return somaTotal
### Função para calcular o percentual #######################################################
def calculaPrecent(lstQtd,lstValorUnit):
    per = 0
    ind = 0
    for x in lstQtd:
        per = per + lstQtd[ind] 
        ind+=1
    per = (100 * (lstQtd[ possuiMais( lstQtd ) ] / per ) )
    return per
### Função para mostrar qual tenis possui mais em estoque ######################################
def possuiMais(lstQtd):
    ind = 0
    val_Atual = 0
    indMaior = 0
    for x in lstQtd:
        if lstQtd[ind] > val_Atual:
            val_Atual = lstQtd[ind]
            indMaior = ind
        ind+=1
    return indMaior
### Função para mostrar o menu ############################################################
def menu():    
    menu ='''
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

### Funcçao que cadastra a cor do tenis ################################################### Cor
def cadCor(lstCor):
    if depoisDeAdicionadoNoEstoque == True:
        print('')
    else:    
            while True:                
                print('\n----- Cor -----')
                mostraListaExemplo(listaCorExemplo)
                escolha  = lerInteiro('Digite o numero da cor que deseja adicionar:  ')
                if escolha > (len(listaCorExemplo)-1) or escolha < 0:
                    print('Item escolhido fora da lista!\n digite o numero de um iten  que esteja na  lista!')
                else:
                    lstCor.append(listaCorExemplo[escolha])
                    break

### Função que cadastra a numeração do tenis ######################################### Numeracao
def cadNumeracao(lstNumeracao):
    if depoisDeAdicionadoNoEstoque == True:
        print('')
    else:  
            while True:            
                print('\n-------- Numeracao --------')
                numeracao = lerInteiro('Digite a numeracao do tenis [ 22 - 46]: ') 
                if numeracao >= 22 and numeracao <= 46 :
                    lstNumeracao.append(numeracao)
                    break
                else:
                    print('Erro digite um numero no intervalo de 22 ate 48\nDigite novamento um Numero!')

### Função que cadastra a quantidade de tenis que terá no estoque ########################## Quantidade
def cadQuantidade(lstQtd):
    if depoisDeAdicionadoNoEstoque == True:
        print('')
    else:  
            while True:
                
                print('\n-------- Quantidade --------')                
                quantidade = lerInteiro('Digite a quantidade de tenis: ') 
                if quantidade == 0 or quantidade < 0 or quantidade > 500:
                    print('Quantidade muito alta ou muito baixa\nDigite novamente!')
                else:
                    lstQtd.append(quantidade)
                    break

### Função que cadastra o valor do tenis ################################################## Valor
def cadValor(lstValorUnit):
    if depoisDeAdicionadoNoEstoque == True:
        print('')
    else:  
            while True:
                
                print('\n-------- Valor --------')
                valor = lerInteiro('Digite o valor do tenis: ') 
                if valor <= 10 or valor > 5000:
                    print('Valor não digitado ou muito grande')
                else:
                    lstValorUnit.append(valor)
                    break

### Função para perguntar se deseja cadastrar novamente ######################################## 
def cadNovamente():
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    resposta  = input('Deseja adicionar mais tenis?\nS = SIM ou N = NAO: ')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    if resposta.upper() == 'S' or resposta.upper() == 'SIM':
        cadastroTotal()
    elif resposta.upper() != 'S' or resposta.upper() != 'SIM':
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('------------------- FIM DO CADASTRO ------------------- ')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        
        

### Funcção que efetua o cadastro chamando cada função que desenpenha uma parte do cadastro ####### 
def cadastroTotal():
    depoisDeAdicionadoNoEstoque = False
    while True:
        print('\n-------- Modelo --------')
        mostraListaExemplo(modeloExemplo)
        modelo  = lerInteiro('Digite o numero do modelo do tenis: ')
        if modelo >= 0 and modelo <= len(lstModelo)-1:
            if modeloExemplo[modelo] in lstModelo:
                print('\n ------------ Esse modelo ja existe! ------------\n Você deseja adicionar mais no desse modelo \n no estoque ou quer adicionar outro novo?')
                print(' -----------------------------------------------------\n')

                escolhaEstoque = lerInteiro('\n  1 - Novo  ou  2 - Adicionar mais estoque: ')
                if escolhaEstoque == 2:
                    addEstoque(lstQtd)
                    depoisDeAdicionadoNoEstoque = True
            if int(modelo) > (len(modeloExemplo)-1) or int(modelo) < 0:
                    print('modelo não digitado ou muito grande')
            else:
                if depoisDeAdicionadoNoEstoque == True:
                    break
                else:
                    lstModelo.append(modeloExemplo[int(modelo)])
                    break
        else:
            print('Numero do tenis escolhido está ERRADO\nEscolha novamente!')
    if depoisDeAdicionadoNoEstoque == False:    
        cadCor(lstCor)
        cadNumeracao(lstNumeracao)
        cadQuantidade(lstQtd)
        cadValor(lstValorUnit)
        cadNovamente()
    depoisDeAdicionadoNoEstoque = False

### Relatorio ##############################################################################
def relatorioGeral():
    if len(lstModelo) != 0:
        mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('          Total em Estoque R$:',total(lstQtd,lstValorUnit))
        print('O tenis '+lstModelo[possuiMais(lstQtd)],' é o que possui ',calculaPrecent(lstQtd,lstValorUnit),'% de todo o estoque!')
        print('E só o tenis ',lstModelo[possuiMais(lstQtd)],' que esta parado, possui o valor de  R$',lstQtd[possuiMais(lstQtd)]*lstValorUnit[possuiMais(lstQtd)],' de prejuizo!')
        #print('possuiMais( lstQtd ):',possuiMais( lstQtd ) )
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    else:
        print('\nLista vazia!')
        
### Realizar Venda ##############################################################################
def realizarVenda():
    if len(lstModelo) != 0:
        mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
        while True:
            escolha  = lerInteiro('Escolha um para vender: ')
            if escolha > (len(lstModelo)-1) or escolha < 0:
                    print('Item escolhido fora da lista!\n digite o numero de um iten  que esteja na  lista!')
            else:
                quntidadeVenda  = lerInteiro('Quantos voce deseja vender: ')
                if quntidadeVenda > lstQtd[escolha] or quntidadeVenda <= 0:
                        print('Voce nao tem essa quantidade ou valor digitado esta errado!')
                else:
                    lstQtd[escolha] = lstQtd[escolha] - quntidadeVenda
                    if lstQtd[escolha] == 0:
                        limpaItem(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit,escolha)

                    print('Venda realisada com sucesso\n')
                    print('---- LISTA ATUALIZADA ----')
                    mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
                    break
        else:
            print('\nLista vazia!')
### Função para atualizar o preço (Opção 6) ################################################
def atulizaPreco():        
        if len(lstModelo) != 0:
            mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
            while True:
                escolha  = lerInteiro('Digite o numero de um item que deseja atualizar o preco:  ')

                if escolha > (len(lstModelo)-1) or escolha < 0:
                    print('Item escolhido fora da lista!\n digite o numero de um iten  que esteja na  lista!')
                else:
                    precoAtual  = lerInteiro('Qual o valor atualizado que deseja inserir:  ')
                    if precoAtual <= 0 or precoAtual > 10000:
                        print('Esse preco é muito elevado ou valor digitado esta errado!')
                    else:
                        lstValorUnit[escolha] = precoAtual
                        print('Preço atualizado com sucesso\n')
                        print('---- LISTA ATUALIZADA ----')
                        mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
                        break
        else:
            print('\nLista vazia!')
### Função para cadastrar cores ( Opção 5 ) ###############################################
def cadastrarCores():
    while True:
        #mostraListaExemplo(lstCor)
        print('\n----- Cor -----')
        cor  = input('Digite a Cor que deseja cadastrar: ')
        if len(cor) == 0 or len(cor)> 20:
            print('Cor não digitada ou muito grande')
        else:
            listaCorExemplo.append(cor)
            print('---- LISTA ATUALIZADA ----')
            mostraListaExemplo(listaCorExemplo)
            break

#################################################################################
def addEstoque(lstQtd):
    mostraLista(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
    
    while True:
        
        escolha = lerInteiro('Escolha um para adicionar mais em estoque: ')
        if escolha >= 0 and escolha <= len(lstModelo)-1:
            quantidadeAdd = lerInteiro('Quanto deseja adicionar: ')
            if quantidadeAdd <= 0 and quantidadeAdd>500:
                print('Numero deve ser maior que 0 (Zero) e menor que 500 (Quientos)')
            else:
                print('lstQtd[escolha] = ',lstQtd[escolha])
                print('(lstQtd[escolha]+quantidadeAdd) = ',(lstQtd[escolha]+quantidadeAdd))
                print('quantidadeAdd = ',quantidadeAdd)
                lstQtd[escolha] = (lstQtd[escolha]+quantidadeAdd)
                break
        else:
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('Esse Tenis não existe\nDigite o numero que conste na lista')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')

#################################################################################
def guardaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit):
    if(len(lstModelo) != 0):
        
        fileName = input("\nQual o nome do banco de dados deseja exportar?\nOu tecle [ENTER] para usar a padrão ")
        fileName = fileName + ".txt"

        if(fileName != ''):
            file1 = open(fileName,"w")
        else:
            if os.path.isfile("sapataria_dados.txt"):
                file1 = open("sapataria_dados.txt", "r")
            else:
                print('Esse banco de dados não existe!')
                guardaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)
            
        ind = 0    

        for x in range(len(lstModelo)):
            file1.write(lstModelo[x]+' '+str(lstNumeracao[x])+' '+str(lstQtd[x])+' '+str(lstValorUnit[x])+' '+lstCor[x]+'\n')
            ind += 1

        file1.close()
        print('----- Armazenado no TXT sucesso! -----')
    
    else:
        print("\nNão existe item nas listas para armazenar no txt!\n")

#################################################################################
def recuperaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit):
    fileName = input("\nQual o nome do banco de dados deseja importar?\nOu tecle [ENTER] para usar a padrão ")
    fileName = fileName + ".txt"

    if(fileName != '.txt'):
        dados = open(fileName,"r")
    else:
        if os.path.isfile("sapataria_dados.txt"):
            dados = open("sapataria_dados.txt", "r")
        else:
            print('Esse banco de dados não existe!')
            recuperaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)

        

    #Efetua a leitura das linhas do arquivo
    for line in dados.readlines():
        #Quebra a linha lida em uma lista, a cada espaço encontrado é gerado um item na lista
        sapato = line.strip().split(' ')
        #print(sapato)
        lstModelo.append(sapato[0])
        lstNumeracao.append(int(sapato[1]))
        lstQtd.append(int(sapato[2]))
        lstValorUnit.append(float(sapato[3]))
        lstCor.append(sapato[4])

    print('----- Importado do TXT com sucesso! -----')
    dados.close()

    

###  Execução ######################################################################
while True:
    escolha = lerInteiro(menu())

    if escolha == 0:
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('_____________FIM_____________\n_______Ate logo amigo!_______')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        break
    
    elif escolha == 1:
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 1 - Cadastro -----------')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        cadastroTotal()
        
    elif escolha == 2:
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 2 - Relatorio ----------')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        relatorioGeral()
        
    elif escolha == 3:
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 3 - Realizar Venda -----')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        realizarVenda()
        
    elif escolha == 4:
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('----- Opcao 4 - Atualizar preços -----')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        atulizaPreco()

        
    elif escolha == 5:
         print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
         print('----- Opcao 5 - Cadastrar Cores -----')
         print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
         cadastrarCores()

    elif escolha == 6:
         print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
         print('----- Opcao 5 - Cadastrar no TXT -----')
         print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
         guardaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)

    elif escolha == 7:
         print('\n-------------------------------------------------------------------------------------------------------------------------------------------------------------')
         print('----- Opcao 5 - Recuperar no TXT -----')
         print('-------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
         recuperaTxt(lstModelo, lstCor, lstNumeracao, lstQtd, lstValorUnit)

    else:
        print('Item do menu inexistente')








