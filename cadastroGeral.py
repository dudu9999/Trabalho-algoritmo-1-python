import tenis
import validacao
from produto import Produto


def CadastroGeral(listaProdutos):
    t = tenis.Tenis()
    t.set_modelo(validacao.validaCadastroModelo())
    t.set_numeracao(validacao.validaCadastroNumeracao())
    t.set_cor(validacao.validaCadastroCor())

    prod = Produto()
    prod.set_quantidade(validacao.validaCadastroQuantidade())
    prod.set_valor(validacao.validaCadastroValor())
    prod.set_tenis(t)

    listaProdutos.append(prod)
