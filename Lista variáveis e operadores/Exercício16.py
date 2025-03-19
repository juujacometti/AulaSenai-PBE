#  Crie quatro variáveis, x1, y1, x2 e y2, representando as coordenadas de dois pontos no plano cartesiano (por exemplo, x1 = 1, y1 = 2, x2 = 4, y2 = 6). Os valores devem ser solicitados pelo usuário. Calcule a distância entre esses dois pontos usando a fórmula da distância euclidiana

x1 = float(input("Digite o valor x da primeira coordenada:\n"))
y1 = float(input("Digite o valor y da primeira coordenada:\n"))
x2 = float(input("\nDigite o valor x da segunda coordenada:\n"))
y2 = float(input("Digite o valor y da segunda coordenada:\n"))

distancia = ((x2 - x1) **2 + (y2 - y1) **2) **0.5

print(f"A distância entre dois pontos é: {distancia}")
