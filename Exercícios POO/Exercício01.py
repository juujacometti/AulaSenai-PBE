"""
1. Criar a classe Produto com os atributos: * nome / * preco -> privado
2. Implemente um método para exibir_dados(), que imprime o nome e o preço
3. Crie os getter e setter do preço
4. Criar classe Carrinho com: * atributo itens (lista, inicialmente vazia)
5. Métodos da classe Carrinho: * adicionar(produto) - recebe um Produto e adiciona a lista itens / * remover(produto) - remove o produto da lista itens / * total - retorna a soma dos
    preços dos produtos no carrinho / * listar_itens() - imprime todos os produtos com seu preço
"""

# Criação da classe Produto
class Produto:
    def __init__(self, nome, preco):
        # Atributos
        self.nome = nome    # Atributo público
        self.__preco = preco    # Atributo privado "__"
        
    # Função para exibição dos dados criados 
    def exibir_dados(self): 
        print(f"Nome produto: {self.nome} e Preço produto: {self.__preco}")
        
    @property       # Criação da propriedade preço 
    def preco(self):    # Getter para acessar o preço
        return self.__preco     
    
    @preco.setter
    def preco(self, novo_preco):    # Setter para definir um novo preço/ preço inválido
        if preco < 0:
            raise ValueError ("Inválido")
        
        self.__preco = novo_preco
            
#Adicionar e Remover
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def remover(self,produto):
        self.itens.remove(produto)
        
    def total(self):
        soma = 0
        for produto in self.itens:
            soma += produto.preco
        return soma

    def listar_itens(self):
        print("Itens no carrinho:")
        for produto in self.itens:
            produto.exibir_dados()
        print(f"Total: R${self.total():.2f}")

#Criação dos produtos presentes no carrinho
produto1 = Produto("Energético", 10)
produto2 = Produto("Chocolate", 5)
produto3 = Produto("Pastel de queijo", 13)

#Adiciono ao objeto carrinho com a Classe Carrinho
carrinho = Carrinho()
carrinho.adicionar(produto1)
carrinho.adicionar(produto2)
carrinho.adicionar(produto3)

carrinho.listar_itens()