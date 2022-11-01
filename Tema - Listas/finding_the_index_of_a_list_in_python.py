"""
Localizando o índice de uma lista em python:

Metodo/função:  variável = lista.index('')

Esse método pode ser utilizado para encontrar o valor do índice de um item que está em uma lista.
"""

# Exemplo Prático - Consultando o valor de um produto com base em outra lista:

# Lista 1 - Produtos de uma padaria:
from operator import index


prod_padaria = ["Pão Francês", "Presunto", "Mussarela", "Oreo", "Coxinha", "Leite", "Biz"]

# Lista 2 - Preço dos Produtos
preco_prod = [0.20, 5.00, 10.00, 2.50, 3.00, 4.00, 6.00]

# Encontrando o índice da "Coxinha" e depois imprimindo o seu valor:
i = prod_padaria.index("Coxinha")
print(preco_prod[i]) # Print do índice 'i', que é o indice da coxinha (4). -> Valor do print: 3.00

# Desafio proposto:
# Script que valida a quantidade de produto de acordo com a informação cedida pelo usuário;



# lista produto
produto = ['arroz', 'feijão', 'macarrão', 'ovo', 'bife', 'cenoura']

# lista quantidade produto
qntd_produto = [5, 20, 15, 200, 50, 100]

# Solicita o Nome do produto;
qt_produto = input('Informe o nome do produto:')

# Valida se o produto está contido na lista
if qt_produto in produto:
        
    # Valida o índice do item na lista
    i = produto.index(qt_produto)

    # Valida a quantidade de unidades desse produto
    index_prod = qntd_produto[i]
      
    # imprime para o usuário essa quantidade
    print('A quantidade de {}, é de {} unidades.'.format(qt_produto, index_prod))
else:
    print('Este item não está contido na lista')
