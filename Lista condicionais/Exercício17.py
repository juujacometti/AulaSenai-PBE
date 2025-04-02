"""
Valide e converta uma data no formato dd/mm/aaaa para aaaa-mm-dd, verificando se a data é válida.
• Regras de validação:
i. O mês deve ser entre 1 e 12.
ii. O dia deve estar dentro dos limites do mês (como 28, 29, 30 ou 31, dependendo do mês e do ano).
"""

dia = int(input("Digite o dia:\n"))
mes = int(input("Digite o mês:\n"))
ano = int(input("Digite o ano:\n"))

if mes < 1 or mes > 12:
    print("A data digitada está inválida!")
else:
    # Fevereiro
    if mes == 2:
        # Verificação de ano bissexto:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            # Caso o ano seja bissexto:
            if dia < 1 or dia > 29:
                print("A data digitada está inválida!")
            else:
                print(
                    f"\nA data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
        # Caso o ano não seja bissexto:
        else:
            if dia < 1 or dia > 28:
                print("A data digitada está inválida!")
            else:
                print(
                    f"\nA data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
    # Meses com até 31 dias:
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 1 or dia > 31:
            print("A data digitada está inválida!")
        else:
            print(
                f"\nA data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")
    # Meses com até 30 dias:
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 1 or dia > 30:
            print("A data digitada está inválida!")
        else:
            print(
                f"\nA data no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")