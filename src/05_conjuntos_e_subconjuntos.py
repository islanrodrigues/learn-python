# Conjunto é uma coleção de valores distintos.
# Os conjuntos são delimitados por chaves -> {}.
# Os conjuntos não permitem duplicidade de valores, ou seja, caso tente adicionar um elemento já existente no conjunto, ele será desconsiderado.
# Os conjuntos são do tipo set.
# Igualmente na matemática, os conjuntos em Python também permitem operações de união, intersecção etc.
# Uma declaração entre chaves vazias não retorna um conjunto (tipo set) mas sim um dicionário (tipo dict).
conjunto_numeros = {1, 2, 3, 4, 5}
variavel_nao_conjunto = {}

print(type(conjunto_numeros))  # saída -> <class 'set'>
print(type(variavel_nao_conjunto))  # saída -> <class 'dict'>


# Adicionando e removendo um elemento ao conjunto.
conjunto_numeros.add(6)  # resultado -> {1, 2, 3, 4, 5, 6}
conjunto_numeros.discard(1)  # resultado -> {2, 3, 4, 5, 6}


# União entre conjuntos.
conjunto_1 = {1, 2, 3, 5, 7, 9, 9}
conjunto_2 = {0, 2, 2, 4, 6, 7, 8}

conjunto_uniao = conjunto_1.union(conjunto_2)
print(conjunto_uniao)  # saída -> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# Intersecção entre conjuntos.
conjunto_interseccao = conjunto_1.intersection(conjunto_2)
print(conjunto_interseccao)  # saída -> {2, 7}


# Diferença entre conjuntos.
conjunto_diferenca_1 = conjunto_1.difference(conjunto_2)
print(conjunto_diferenca_1)  # saída -> {1, 3, 5, 9}

conjunto_diferenca_2 = conjunto_2.difference(conjunto_1)
print(conjunto_diferenca_2)  # saída -> {0, 8, 4, 6}


# Diferença simétrica entre conjuntos, ou seja, elimina todos os elementos que aparecem em ambos os conjuntos.
conjunto_dif_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print(conjunto_dif_simetrica)  # saída -> {0, 1, 3, 4, 5, 6, 8, 9}


# Verificando se um conjunto é um subconjunto de outro.
conjunto_3 = {1, 3, 5}

is_subconjunto_1_2 = conjunto_1.issubset(conjunto_3)
is_subconjunto_3_1 = conjunto_3.issubset(conjunto_1)

print(is_subconjunto_1_2)  # saída -> False
print(is_subconjunto_3_1)  # saída -> True


# Verificando se um conjunto é um superconjunto de outro.
conjunto_4 = {2, 6, 8}

is_superconjunto_2_4 = conjunto_2.issuperset(conjunto_4)
is_superconjunto_4_2 = conjunto_4.issuperset(conjunto_2)

print(is_superconjunto_2_4)  # saída -> True
print(is_superconjunto_4_2)  # saída -> False


# Convertendo uma lista em um conjunto através da função built in set().
lista_animais = ["cachorro", "gato", "cachorro", "passarinho", "galinha", "gato"]

conjunto_animais = set(lista_animais)
print(conjunto_animais)