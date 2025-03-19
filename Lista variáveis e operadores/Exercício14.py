#  Crie duas variáveis, a e b, com valores escolhidos pelo usuário. Troque os valores dessas variáveis sem usar uma terceira variável e imprima os novos valores de a e b.

a = int(input("Digite um número inteiro:\n"))
b = int(input("Digite um segundo número inteiro:\n"))

a, b = b, a

print("\n",a,"\n",b)
