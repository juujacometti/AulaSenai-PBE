# Um matemático precisa calcular fatoriais para números em um estudo, mas só pode usar números positivos. Para o estudo do matemático é necessário calcular o fatorial de 3,7,9,25,26

def fatorial(numero):
    if numero < 0:
        print(f"O número é inválido. Tente digitar um número positivo.")
        
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
            
        print(f"O fatorial de {numero} é: {resultado}")
            
    return resultado

fatorial(3)
fatorial(7)
fatorial(9)
fatorial(25)
fatorial(26)