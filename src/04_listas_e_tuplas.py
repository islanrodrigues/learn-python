# Listas são delimitadas por colchetes -> []
# Listas são mutáveis.
lista_numeros = [1, 5, 7, 9, 3]
lista_animais = ["cachorro", "gato", "papagaio", "rato", "cobra", "cavalo"]

print(lista_numeros[0], lista_animais[0])  # saída -> 1 cachorro
print(lista_numeros[1], lista_animais[1])  # saída -> 5 gato


# sum() é uma função built in que permite fazer a somatória de todos os elementos de uma lista.
print(sum(lista_numeros))  # saída -> 25


# Iterando uma lista
for animal in lista_animais:
  print(animal)


# min() e max() são funções built in que permite retornar os elementos de mínimo e máximo de uma lista, respectivamente.
min(lista_numeros)  # 1
max(lista_numeros)  # 9

min(lista_animais)  # cachorro
max(lista_animais)  # rato


# Verificando se já existe um determinado elemento na lista, e se não existe adiciona.
if 'lobo' in lista_animais:
  print("Já existe lobo na lista")

else:
  print("Ainda não existe lobo na lista")
  lista_animais.append("lobo")


# Removendo um elemento da lista.
lista_numeros.pop(4)  # Removendo pelo indíce
lista_numeros.remove(7)  # Removendo pelo elemento


# Ordenando uma lista.
lista_animais.sort()
print(lista_animais)


# Revertendo a ordem atual da lista
lista_animais.reverse()


print("- - - - - - - - - - - - - - - - - -")


# Tuplas são delimitadas por parênteses -> ().
# Tuplas são imutáveis.
tupla_numeros = (8, 2, 6, 4, 0)

print(tupla_numeros[2])  # saída -> 6


# tuple() é uma função built in que permite converter uma lista para uma tupla
tupla_animais = tuple(lista_animais)
print(tupla_animais)