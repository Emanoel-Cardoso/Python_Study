"""
Índices em Lista:

Objetivos - Aprender:
    > Entender como funciona a posição de um valor/parâmetro da lista;
    > Alterar um valor de uma lista;
    
Observação: Em Python, o índice de uma lista sempre terá início para partir do 0. Portanto, o primeiro valor da lista sempre terá o índice 0.
  
"""
# Exemplo - Itens de um computador:
computador_itens = ["monitor", "teclado", "mouse", "gabinete", "cabos"]

print(computador_itens[4]) # cabos
print(computador_itens[0]) # monitor

# Alterando o valor do indice 2
computador_itens[2] = "mousepad"
print(computador_itens[2]) # mousepad

"""
Observação 2: A string em Python é considerada uma lista imutável (). Diferente de uma lista que você pode editar da formar que quiser.


# Exemplo - String:
nome = "Emanoel"
nome[0] = "A"
print(nome) 
# Ao tentar executar o seguinte erro é notificado: " 'str' object does not support item assignment / O objeto 'str' não suporta atribuição de item. "

"""

