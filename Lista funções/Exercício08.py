# Um cientista precisa converter três temperaturas de Celsius para Fahrenheit para um relatório: 30°C, 100°C e 0°C

def fahrenheit(temperatura):
    resultado = (temperatura * 1.8) + 32
    print(f"A temperatura {temperatura} em Fahrenheit é: {resultado}")
    return resultado

fahrenheit(30)
fahrenheit(100)
fahrenheit(0)