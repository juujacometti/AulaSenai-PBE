'''
Implemente a validação de senha diretamente no corpo do código, sem usar funções. Os requisitos para a senha são:
• Pelo menos 8 caracteres.
• Pelo menos uma letra maiúscula.
• Pelo menos uma letra minúscula.
• Pelo menos um número.
• Pelo menos um caractere especial (@, #, $, %, &).
Caso algum critério não seja atendido, exiba uma mensagem dizendo qual critério está faltando.
Dica: Pesquise como utilizar a biblioteca re
'''

import re

senha = input("Digite uma senha:")

if len(senha) < 8:
    print("A senha deve conter no mínimo 8 caracteres. Tente outra vez.")
elif not re.search(r"[A-Z]", senha):
    print("A senha  deve conter pelo menos uma letra maiúscula. Tente outra vez.")
elif not re.search(r"[a-z]", senha):
    print("A senha deve conter pelo menos uma letra minúscula. Tente outra vez.")
elif not re.search(r"\d", senha):
    print("A senha deve conter pelo menos um número. Tente outra vez.")
elif not re.search(r"[^A-Za-z0-9]", senha):
    print("A senha deve ter pelo menos um caractere especial. Tente outra vez.")
else:
    print("Senha registrada com sucesso!")