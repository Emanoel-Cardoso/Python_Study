"""
Adicionar e remover itens de uma lista com python

- Adicionar um item no final da lista - sintax:

    lista.append(item)

- Remover um item da lista - sintax:

    lista.remove(item) "Remove o item informado"
    variavel = lista.pop(index) "Remove o item que está no index informado"
    
    Observação: A diferença entre o método .remove() e .pop() é que no método pop você consegue armazenar o item removido em uma variável.

"""
# Lista de nomes que acabam com el
lista_nome = ["Emanoel", "Gabriel", "Pedro", "Samuel", "Smael"]

# Adicionando o mais um nome com el "Joziel"
lista_nome.append("Joziel")
print(lista_nome)

# Removendo o nome que não termina com El "Pedro"
lista_nome.remove("Pedro")
print(lista_nome)

lista_nome2 = ["Emanoel", "Gabriel", "Pedro", "Samuel", "Smael"]
# removendo com pop

item_removido = lista_nome2.pop(2)
print(item_removido)


