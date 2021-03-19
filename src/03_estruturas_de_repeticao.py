# A função range() é uma função built in, onde pode receber os índices de início e fim e também o percentual de incremento.
# Na função range, caso sejam informados somente os índices, o incremento é considerado como sendo 1 e caso seja informado somente o índice de fim, o índice inicial é considerado como sendo 0.
# Na função range, o índice inicial é inclusivo enquanto o índice final é não inclusivo.

# Imprimir o valor de 0 até 10.
for x in range(0,11, 1):
  print(x)

# Imprimir o valor de 1 até 20.
for y in range(1, 21):
  print(y)


print("- - - - - - - - - - - - -")


# Receber um número e descobrir se ele é primo ou não.
num = int(input("Informe um número inteiro: "))
qntd_divisao = 0

for i in range(1, num + 1):
  resto = num % i

  if resto == 0:
    qntd_divisao += 1

if qntd_divisao == 2:
  print("O número {} é primo".format(num))

else: 
  print("O número {} não é primo".format(num))


print("- - - - - - - - - - - - - -")


# Identificando todos os números primos de 1 até 100.
for i in range(1, 101, 1):
  qntd_divisao = 0

  for j in range(1, i + 1, 1):
    resto = i % j

    if resto == 0:
      qntd_divisao += 1
  
  if qntd_divisao == 2:
    print("{} é primo".format(i))


print("- - - - - - - - - - - - - -")


# Solicitar um número e só aceitar se for um número divisível por 5 utilizando a estrutura while.
divisivel_por_cinco = False

while not divisivel_por_cinco:
  valor = int(input("Informe um número inteiro: "))

  resto = valor % 5

  if resto == 0:
    divisivel_por_cinco = True
    print("{} é divisível por 5.".format(valor))
  
  else:
    print("{} não é divisível por 5.".format(valor))
    print("Tente novamente. \n")