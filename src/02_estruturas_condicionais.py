a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))

# No Python, blocos de código são construídos levando em consideração a indentação do código (TAB).
# É usado o ':' para delimitar blocos, funções etc.

# Condicionais if, else e elif (else - if).
if a > b:
  print("O maior número entre A e B é o A")

else:
  print("O maior número entre A e B é o B")


print("- - - - - - - - - - - - - - -")


if a > b and a > c:
  print("O maior número é o {}".format(a))

elif b > a and b > c:
  print("O maior número é o {}".format(b))

else:
  print("O maior número é o {}".format(c))


print("- - - - - - - - - - - - - - -")


num_1 = int(input("Informe um número inteiro: "))

resto = num_1 % 2

if resto == 0:
  print("{} é par".format(num_1))

else:
  print("{} é ímpar".format(num_1))