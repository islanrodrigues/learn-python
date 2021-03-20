# Dicionário é uma estrutura de dados que permite armazenar elementos conhecidos como objetos, onde cada objeto é dividido entre chave e valor.
# Através da chave é possível identificar cada objeto. Todo objeto obrigatoriamente precisa possuir uma chave.
# Dicionários de dados são delimitados por chaves -> {}.
# Os dicionários são do tipo dict.
animais = {
  "cachorro": {"nome científico": "Canis lupus familiaris", "família": "canidae", "classe": "mammalia"},
  "gato": {"nome científico": "Felis silvestris catus", "família": "felidae", "classe": "mammalia"},
  "porco": {"nome científico": "Sus scrofa domesticus", "família": "suidae", "classe": "mammalia"},
  "galinha": {"nome científico": "Gallus gallus domesticus", "família": "phasianidae", "classe": "aves"},
  "cavalo": {"nome científico": "Equus ferus caballus", "família": "equidae", "classe": "mammalia"}
}

print(type(animais))  # saída -> <class 'dict'>


# Buscando um objeto (retorna o valor correspondente à chave) dentro do dicionário através da informação da chave.
gato = animais.get("gato")
print(gato)

cachorro = animais["cachorro"]
print(cachorro)

cobra = animais.get("cobra")
print(cobra)  # saída -> None


# Eliminando um objeto do dicionário de dados através da informação da chave.
del animais["galinha"]
print(animais)


# Iterando um dicionário de dados.
for chave, valor in animais.items():
  print("O animal da chave {} pertence á família {}".format(chave, valor.get("família")))


# items() é uma função que permite retornar um conjunto de todos os objetos (em forma de tupla) do dicionário.
lista_itens = list(animais.items())
print(lista_itens)


# values() é uma função que permite retornar um conjunto de todos os valores (sem as chaves) de todos os objetos do dicionário.
lista_valores = list(animais.values())
print(lista_valores)


# keys() é uma função que permite retornar um conjunto de todas as chaves (sem os valores) de todos os objetos do dicionário.
lista_chaves = list(animais.keys())
print(lista_chaves)


# popitem() é uma função que permite eliminar o último objeto da lista e retorná-lo em forma de tupla.
pessoas = {
  "pedro": ["Pedro da Silva", "23/06/2000", "Estagiário de Marketing"],
  "maria": ["Maria Oliveira", "20/09/1990", "Advogada"],
  "joão": ["João de Andrade", "19/01/1995", "Dentista"],
  "juliana": ["Juliana Alves", "14/11/2001", "Estudante"]
}

ultimo_integrante = pessoas.popitem()

print(pessoas)
print(ultimo_integrante)  # saída -> ('juliana', ['Juliana Alves', '14/11/2001', 'Estudante'])


# clear() é uma função que permite esvaziar por completo o dicionário.
pessoas.clear()
print(pessoas)  # saída -> {}


print("- - - - - - - - - - - - - - -")


# Strings em Python são imutáveis. Dessa forma, não é possível alterar atribuindo um valor através do índice.

# Iterando uma String como se fosse uma lista.
texto = "Python é uma linguagem de programação bacana!"

for letra in texto:
  print(letra)


# Realizando técnica de substring com índices de ínicio (inclusivo) e fim (não inclusivo).
#Quando o índice de fim não é declarado, o índice de fim é considerado o índice final da String.
nome_linguagem = texto[0:6]
print(nome_linguagem)  # saída -> Python

adjetivo_linguagem = texto[13:]
print(adjetivo_linguagem)  # saída -> linguagem de programação bacana!


'''
É possível realizar substrings com a lógica inversa dos índices, ou seja, considerando o fluxo do fim da string até o seu início.
Exemplo:
          u m a   f r a s e  =  u  m  a     f  r  a  s  e
          0 1 2 3 4 5 6 7 8    -9 -8 -7 -6 -5 -4 -3 -2 -1
'''
sub_indice_invertido = texto[-45:-23]
print(sub_indice_invertido)  # saída -> Python é uma linguagem


# Invertendo uma string.
texto_invertido = texto[::-1]
print(texto_invertido)


# Fatiando uma string através do método split(), onde o parâmetro é a string delimitadora.
lista_palavras = []
frase = "No pain no gain"

lista_palavras = frase.split(" ")
print(lista_palavras)

frase = "Sem dor, sem ganho"
lista_palavras = frase.split(",")
print(lista_palavras)
