# Solicite ao usuário três lados e determine se é possível formar um triângulo. Em caso afirmativo, diga se é equilátero, isósceles ou escaleno

lado1 = float(input("Informe três valores para saber se eles formam um triângulo e se formarem, qual a sua classificação.\nDigite o primeiro valor:\n"))
lado2 = float(input("Digite o segundo valor:\n"))
lado3 = float(input("Digite o terceiro valor:\n"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os valores digitados podem formar um triângulo.")

    if lado1 == lado2 and lado1 == lado3:
        print("Os valores digitados formam um triângulo.\nClassificação: EQUILÁTERO")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores digitados formam um triângulo.\nClassificação: ISÓSCELES")

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Os valores digitados formam um triângulo.\nClassificação: ESCALENO")

else:
    print("Os valores digitados não podem formar um triângulo.")