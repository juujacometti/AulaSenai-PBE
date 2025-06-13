"""
Crie uma classe RelatorioBiblioteca que gera relatórios sobre a biblioteca, recebendo um objeto Biblioteca no construtor. Implemente os seguintes métodos:
• gerar_relatorio_completo(): Retorna uma string com informações detalhadas de todos os itens (usando obter_info()). 
• gerar_relatorio_disponibilidade(): Retorna uma string com os títulos dos itens disponíveis e o total de itens disponíveis. 
• gerar_relatorio_emprestimos(): Retorna uma string com o número de itens emprestados e a proporção de itens emprestados em relação ao total
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
    
# Parte exercício 4
class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item):
        if item.titulo in self.itens:
            raise Exception("Já existe um item com este título na biblioteca.")
        self.itens[item.titulo] = item

    def remover_item(self, titulo):
        if titulo not in self.itens:
            raise Exception("Item não encontrado na biblioteca.")
        del self.itens[titulo]

    def listar_itens_disponiveis(self):
        # Lista para guardar os livros disponíveis
        disponiveis = []  
        for titulo in self.itens:
            item = self.itens[titulo]
            if item.disponivel:
                disponiveis.append(titulo)
        return disponiveis

    def contar_itens_emprestados(self):
        contador = 0
        for item in self.itens.values():
            if not item.disponivel:
                contador += 1
        return contador
    
# Parte exercício 5
class RelatorioBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        relatorio = ""
        for item in self.biblioteca.itens.values():
            relatorio += item.obter_info() + "\n"
        return relatorio.strip()

    def gerar_relatorio_disponibilidade(self):
        disponiveis = self.biblioteca.listar_itens_disponiveis()
        return f"Itens disponíveis: {', '.join(disponiveis)}\nTotal: {len(disponiveis)}"

    def gerar_relatorio_emprestimos(self):
        total = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens_emprestados()
        proporcao = (emprestados / total) * 100 if total > 0 else 0
        return f"Emprestados: {emprestados}\nProporção: {proporcao:.1f}%"
