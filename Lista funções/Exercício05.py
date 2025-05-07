# Um sistema de cinema precisa verificar se três clientes (15, 20 e 8 anos) podem assistir a um filme para maiores de 18 anos

def filme(idade):
    if idade < 18:
        print("Você não tem idade o suficiente para ver esse filme. \nClassificação: +18\n")
    else:
        print("Você pode assistir o filme.\n")

filme(15)
filme(20)
filme(8)
