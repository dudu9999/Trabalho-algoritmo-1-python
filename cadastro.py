import validacao
import tenis

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


