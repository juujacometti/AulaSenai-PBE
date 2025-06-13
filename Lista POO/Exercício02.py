"""
 Crie uma classe ColecaoLivros que herda de ItemBiblioteca para representar uma coleção de livros (ex.: uma trilogia). A coleção é composta por vários objetos ItemBiblioteca. Implemente os seguintes métodos:
• adicionar_livro(livro): Adiciona um objeto ItemBiblioteca à coleção.
• verificar_disponibilidade_colecao(): Retorna True apenas se todos os livros da coleção estiverem disponíveis. 
• Sobrescreva o método obter_info() para incluir a lista de títulos dos livros na coleção
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
        super().__init__(titulo, ano_publicacao) #super() - traz as informações da classe mãe.
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