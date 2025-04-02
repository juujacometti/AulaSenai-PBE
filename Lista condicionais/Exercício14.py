# Pergunte ao usuário uma data no formato "dd/mm/aaaa" e converta para o formato "aaaa-mm-dd"

dia = int(input("Digite o dia de hoje:\n"))
mes = int(input("Digite o mês atual:\n"))
ano = int(input("Digite o ano em que estamos:\n"))

print(
    f"\nA data de hoje no formato dd/mm/aaaa é {dia}/{mes}/{ano}.\nA data de hoje no formato aaaa/mm/dd é {ano}/{mes}/{dia}.")