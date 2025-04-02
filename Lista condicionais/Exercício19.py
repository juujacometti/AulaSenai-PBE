'''
Implemente um código que:
• Solicite ao usuário um número de CPF (Cadastro de Pessoa Física).
• Verifique se o número de CPF possui 11 dígitos (caso contrário, deve retornar "CPF inválido").
• Valide o CPF com base nos dois dígitos verificadores
i. O CPF é composto por 9 dígitos principais (XXXXXXXXX) seguidos por 2 dígitos verificadores (XX), no formato XXX.XXX.XXX-XX.
ii. O primeiro dígito verificador é calculado de acordo com os 9 primeiros dígitos.
iii. O segundo dígito verificador é calculado com base nos 10 primeiros dígitos (9 principais e o primeiro dígito verificador).
Regras de Cálculo dos Dígitos Verificadores:
• Primeiro Dígito Verificador:
i. Multiplicar os 9 primeiros números do CPF pelos pesos: [10, 9, 8, 7, 6, 5, 4, 3, 2].
ii. Somar os resultados.
iii. Dividir a soma por 11 e considerar o resto dessa divisão.
iv. Se o resto for menor que 2, o primeiro dígito verificador será 0.
Caso contrário, subtraímos o resto de 11 para encontrar o primeiro dígito verificador
• Segundo Dígito Verificador:
i. Multiplicar os 10 primeiros números (9 principais e o primeiro dígito verificador) pelos pesos: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2].
ii. Somar os resultados.
iii. Dividir a soma por 11 e considerar o resto dessa divisão.
iv. Se o resto for menor que 2, o segundo dígito verificador será 0. Caso contrário, subtraímos o resto de 11 para encontrar o segundo dígito verificador. Se o CPF for válido, o programa deve retornar a mensagem "CPF Válido". Caso contrário, exiba "CPF Inválido"
'''

import re

cpf = input("Digite o seu CPF:\n")

# Padrão de digitação do cpf
padrao = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"

# Verifica se o cpf digitado está dentro do padrão
valido = re.match(padrao, cpf)

if valido:
    penultimo_digito = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    ultimo_digito = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if penultimo_digito >= 2:
        digito1 = 11 - penultimo_digito
    else:
        digito1 = 0
    if ultimo_digito >= 2:
        digito2 = 11 - ultimo_digito
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print("O CPF é válido!")
    else:
        print("O CPF é inválido!")
else:
    print("O CPF não foi digitado corretamente!")
