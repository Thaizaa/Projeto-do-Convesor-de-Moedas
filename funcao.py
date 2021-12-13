from forex_python.converter import CurrencyRates, CurrencyCodes


def trata_valor(valor: str):
    valor_inicial = 0
    try:
        valor_inicial = float(valor.replace(",", "."))
        return valor_inicial
    except:
        valor_inicial = 0
        print("Valor invalido")
        return valor_inicial


def converte(valor: float, primeira_moeda: str, segunda_moeda: str):
    c = CurrencyRates()
    try:
        valor_convertido = c.convert(primeira_moeda.upper(), segunda_moeda.upper(), valor)
        return round(valor_convertido, 2)

    except:
        print("deu erro")
        return 0


def simbolos(segunda_moeda: str):
    cd = CurrencyCodes()
    try:
        return cd.get_symbol(segunda_moeda.upper())
    except:
        return ""


def lista_moedas():
    c = CurrencyRates()
    moedas = c.get_rates("USD").keys()
    lista_de_moedas = list(moedas)
    lista_de_moedas.insert(0, "USD")
    return lista_de_moedas
