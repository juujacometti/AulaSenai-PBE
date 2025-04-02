"""
Implemente o cálculo da raiz quadrada diretamente no código, verificando se o número é negativo ou muito grande.
• Se o número for negativo, exiba "Não é possível calcular a raiz quadrada de um número negativo."
• Se o número for maior que 100, exiba "Número muito grande, reduza para um valor abaixo de 100."
• Caso contrário, calcule e mostre a raiz quadrada, arredondada para 2 casas decimais.
"""

import math

numero = int(input("Digite um número para saber a raiz quadrada dele:\n"))

if numero < 0:
    print("O número digitado é negativo. Não é possível realizar o calculo da raiz de um número negativo.")
elif numero > 100:
    print("O número digitado é muito grande. Reduza para um valor abaixo de 100.")
else:
    raiz = math.sqrt(numero)
    resultado = round(raiz, 2)
    print(f"A raíz quadrada de {numero} é {resultado}")