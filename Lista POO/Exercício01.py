"""
Crie uma classe ItemBiblioteca para representar um item genérico na biblioteca (como um livro ou revista). 
A classe deve ter os seguintes atributos:
• titulo: String com o título do item.
• ano_publicacao: Inteiro com o ano de publicação (deve ser maior que 0).
• disponivel: Booleano indicando se o item está disponível para empréstimo.

Métodos:
• emprestar(): Marca o item como não disponível, lançando uma exceção se já estiver 
emprestado.
• devolver(): Marca o item como disponível, lançando uma exceção se já estiver disponível.
• obter_info(): Retorna uma string com o título, ano e status de disponibilidade (ex.: "Título: Dom Quixote, Ano: 1605, Disponível: Sim").
"""

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