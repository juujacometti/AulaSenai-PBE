# Um editor de livros quer verificar se algumas palavras de um manuscrito são palíndromos (para título de capítulos). Verifique se os titulos que ele colocou são palíndromos: “Ana Ana”, “1DSTB-SENAI”, “Subi no Onibus”.

def palindromo(palavra):
    palavra_minuscula = palavra.lower()
    if palavra_minuscula == palavra_minuscula[::-1]:
        print(f"A palavra {palavra} é um palíndromo")
        
    else:
        print(f"A palavra {palavra} não é um palíndromo")
        
palindromo("Ana Ana")
palindromo("1DSTB-SENAI")
palindromo("Subi no Onibus")