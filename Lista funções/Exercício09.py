# Um jogo de RPG classifica números como "Pequeno", "Médio" ou "Grande" para definir a dificuldade de um desafio. Classifique os números 3, 9 e 12

def tamanho_numero(numero):
    if numero <= 5:
        print(f"O número {numero} é pequeno.")
        
    elif numero <=10:
        print(f"O número {numero} é médio.")
    
    else:
         print(f"O número {numero} é grande.")
                
tamanho_numero(3)
tamanho_numero(9)
tamanho_numero(12)