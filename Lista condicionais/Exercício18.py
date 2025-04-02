"""
Implemente a validação de senha diretamente no corpo do código, sem usar funções. Os requisitos para a senha são:
• Pelo menos 8 caracteres.
• Pelo menos uma letra maiúscula.
• Pelo menos uma letra minúscula.
• Pelo menos um número.
• Pelo menos um caractere especial (@, #, $, %, &).
Caso algum critério não seja atendido, exiba uma mensagem dizendo qual critério está faltando.
Dica: Pesquise como utilizar a biblioteca re
"""

expressao = str(input("Digite uma expressão matemática para saber o resultado:\n"))
resultado = eval(expressao)

print(f"O resultado da expressão {expressao} é = {resultado}")