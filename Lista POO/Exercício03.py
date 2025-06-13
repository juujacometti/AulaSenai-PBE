"""
Crie uma classe Revista que herda de ItemBiblioteca para representar revistas, que possuem um número de edição. Implemente os seguintes métodos:
• atualizar_edicao(nova_edicao): Atualiza o número da edição, lançando uma exceção se for menor ou igual a 0. 
• restringir_emprestimo(dias_max): Retorna True se a revista pode ser emprestada por no máximo dias_max dias, considerando que revistas mais antigas (antes de 2000) têm restrição de 7 dias. 
• Sobrescreva o método obter_info() para incluir o número da edição.
"""

# Parte do exercício 1
class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        if ano_publicacao <= 0:
            print("Ano de publicação inválido.")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            Exception("Item já emprestado.")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            Exception("Item já está disponível.")
        self.disponivel = True

    def obter_info(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {status}"   
    
# Parte do exercício 2
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao):
        super().__init__(titulo, ano_publicacao) # Função super() - traz as informações da classe mãe.
        self.livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        # Looping para verificar cada um dos livros
        for livro in self.livros: 
            if not livro.disponivel: 
                return False
            else:
                return True

    def obter_info(self):
        retorno = super().obter_info() 
        for livro in self.livros:
            retorno += f'\n {livro.obter_info()}'
        return retorno
    
# Parte exercício 3
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        if edicao <= 0:
            print("Número da edição inválido.")
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            Exception("Nova edição inválida.")
        self.edicao = nova_edicao

    def restringir_emprestimo(self, dias_max):
        if self.ano_publicacao < 2000:
            return dias_max <= 7
        return True

    def obter_info(self):
        return f"{super().obter_info()}, Edição: {self.edicao}"
    
    