# Pergunte ao usuário um ano e verifique se é bissexto. Lembre-se: um ano é bissexto se for divisível por 4, mas não por 100, a menos que seja divisível por 400

ano = int(input("Digite um ano para saber se ele é bissexto:\n"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")

else:
    print(f"O ano {ano} não é bissexto.")
