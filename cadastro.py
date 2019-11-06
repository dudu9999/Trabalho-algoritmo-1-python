import validacao
import tenis
import main

class Cadastro:
    ### Função de cadastro total ##################################################################
    def cadastroTotal(self ,tenis=None):
        tenis = tenis.Tenis(
            tenis.Tenis.set_modelo(self.cadastroModelo()),
            tenis.Tenis.set_numeração(self.cadastroNumeracao()),
            tenis.Tenis.set_quantidade(self.cadastroQuantidade()),
            tenis.Tenis.get_valor(self.cadastroValor()),
            tenis.Tenis.set_cor(self.cadastroCor()))

        main.listaTenis.append(tenis)

        ### Função de cadastro Modelo ##################################################################
    def cadastroModelo(self):
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
    def cadastroNumeracao(self):
        n = validacao.lerInteiro("Numeração: ")
        return n

    ### Função de cadastro Quantidade ##################################################################
    def cadastroQuantidade(self):
        q = validacao.lerInteiro("Quantidade: ")
        return q

    ### Função de cadastro Valor ##################################################################
    def cadastroValor(self):
        v = validacao.lerInteiro("Valor: ")
        return v

    ### Função de cadastro Cor ##################################################################
    def cadastroCor(self):
        main.mostraListaExemplo(main.listaCorExemplo)
        c = input("Cor: ")
        return c

