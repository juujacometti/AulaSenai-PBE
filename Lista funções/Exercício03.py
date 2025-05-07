# Um jogo de tabuleiro usa um dado de 10 faces. Você precisa verificar se os números 4, 7 e 10 são pares (jogador avança) ou ímpares (jogador recua)

def avancar_recuar(jogada):
    if jogada % 2 == 0:
        print("O valor do dado é par. O jogador deve avançar.")

    else:
        print("O valor do dado é ímpar. O jogador deve recuar.")
    return jogada

avancar_recuar(4)
avancar_recuar(7)
avancar_recuar(10)