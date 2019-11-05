import validacao
import main

class Cadastro:
    def __init__(self):
        self.cadastroTotal()

    ### Função de cadastro total ##################################################################
    def cadastroTotal(self):
        tenis = main.Tenis(
            main.Tenis.set_modelo(cadastroModelo()),
            main.Tenis.set_numeração(cadastroNumeracao()),
            main.Tenis.set_quantidade(cadastroQuantidade()),
            main.Tenis.get_valor(cadastroValor()),
            main.Tenis.set_cor(cadastroCor()))

        main.listaTenis.append(tenis)

    ### Função de cadastro Modelo ##################################################################
def cadastroModelo():
    main.mostraListaExemplo(main.listaModeloExemplo) ('Tradicional', 'Esportivo', 'Caminhada', 'Corrida')
    escolha = str(input("Modelo: "))
    if escolha == '1':
        modelo = 'Tradicional'
    if escolha == '2':
        modelo = 'Esportivo'
    if escolha == '3':
        modelo = 'Caminhada'
    if escolha == '4':
        modelo = 'Corrida'
    return modelo

### Função de cadastro Numeracao ##################################################################
def cadastroNumeracao():
    n = validacao.lerInteiro("Numeração: ")
    return n

### Função de cadastro Quantidade ##################################################################
def cadastroQuantidade():
    q = validacao.lerInteiro("Quantidade: ")
    return q

### Função de cadastro Valor ##################################################################
def cadastroValor():
    v = validacao.lerInteiro("Valor: ")
    return v

### Função de cadastro Cor ##################################################################
def cadastroCor():
    main.mostraListaExemplo(main.listaCorExemplo)
    c = input("Cor: ")
    return c

