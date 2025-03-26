# Pergunte ao usuário sua idade e informe se ele tem voto obrigatório, opcional ou não tem voto (menos de 16 anos)

idade = int(input("Digite a sua idade:\n"))

if (idade < 16):
    print("Você ainda não é um eleitor :(")

elif (idade >= 16 and idade < 18):
    print("Você é um eleitor de voto OPCIONAL.")
    
else:
    print("Você é um eleitor de voto OBRIGATÓRIO.")
