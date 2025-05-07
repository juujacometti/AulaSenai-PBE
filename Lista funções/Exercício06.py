# Uma loja está aplicando 10% de desconto em três produtos. Calcule o preço final de cada um: • Produto 1: R$ 50,00 / • Produto 2: R$ 120,00 / • Produto 3: R$ 200,00

def desconto(produto):
    resultado = produto - (produto * 0.10)
    print(f"Preço do produto: {produto}\nPreço com desconto: {resultado}\n")
    return resultado

desconto(50.00)
desconto(120.00)
desconto(200.00)