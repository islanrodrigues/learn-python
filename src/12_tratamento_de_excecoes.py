# Forçando uma divisão por zero (ZeroDivisionError: division by zero)
# Bloco try - except
try:
  divisao = 10 / 0

except ZeroDivisionError:
  print("Não é possível dividir por zero.")  


print("- - - - - - - - - - - -")


# Encadeando várias tratativas de exceções em um mesmo bloco try - except.
try:
  # divisao = 10 / 0
  divisao = 10 / 2

  lista = [1, 2, 3]

  # item = lista[9]
  item = lista[1]

  x = a

except ZeroDivisionError:
  print("Não é possível dividir por zero.")
except IndexError:
  print("Foi tentado acessar um índice que não existe na lista.")
except NameError:
  print("Houve a chamada de uma variável não definida.")
except:
  print("Erro genérico.")


print("- - - - - - - - - - - -")


# BaseException é a classe pai de todas as exceções.
# Exception é uma filha direta de BaseException onde a partir dela se tema a grande maioria das principais classes de exceções. 
try:
  y = b

except BaseException as ex:
  print("Com BaseException...Houve um erro:", ex)

try:
  y = b

except Exception as ex:
  print("Com Exception...Houve um erro:", ex)


print("- - - - - - - - - - - -")


# Bloco try - except - else
# O bloco 'else' é executado somente quando não ocorre nenhuma exceção.
try:
  divisao = 10 / 0
except:
  print("Rolou um erro!")
else:
  print("Não rolou nenhum erro!")

try:
  divisao = 10 / 2
except:
  print("Rolou um erro!")
else:
  print("Não rolou nenhum erro!")


print("- - - - - - - - - - - -")


# Bloco try - except - finally
# O bloco 'finally' sempre irá executar, independente se ocorreu exceção ou não.
try:
  a = b
except:
  print("Rolou um erro!")
finally:
  print("Sempre executa este bloco!")

try:
  a = 10
  b = a
except:
  print("Rolou um erro!")
finally:
  print("Sempre executa este bloco!")


print("- - - - - - - - - - - -")


# Criando uma exceção personalizada.
# Por convenção, toda classe de exceção termina com 'Error'.
# Para forçar o estouro dde uma exceção, é usado o comando 'raise'.
class Error(Exception):
  pass

class CustomExceptionError(Error):
  def __init__(self, message):
    self.message = message


while True:
  try:
    numero = int(input("Entre com um número entre 1 e 10: "))

    if numero < 1 or numero > 10:
      raise CustomExceptionError("O número não pode ser menor que 1 ou maior que 10!")
    
    print("O número digitado foi {}".format(numero))
    break

  except ValueError:
    print("O valor digitado não é um número. Tente novamente.\n\n")
  except CustomExceptionError as ex:
    print(ex)
    print("Tente novamente. \n\n")