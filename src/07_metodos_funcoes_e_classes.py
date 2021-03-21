# Método em Python é todo bloco de código que pode ou não receber parâmetros e que SEMPRE retorna valores.
# Função em Python é todo bloco de código que pode ou não receber parâmetros e que NUNCA retorna valores.

# Para declaração de métodos e funções é usado a palavra reservada 'def'.
def soma(a, b):
  return a + b

def sub(a, b):
  return a - b

def imprime_soma(a, b):
  print(soma(a, b))

def imprime_sub(a, b):
  print(sub(a, b))

imprime_soma(15, 5)  # saída -> 20
imprime_sub(20, 10)  # saída -> 10


# Funções lambda são funções anônimas, que funcionam da mesma forma que funções convencionais, criadas a partir da palavra reservada 'lambda'.
soma_lambda = lambda a, b: a + b
sub_lambda = lambda a, b: a - b

print(soma_lambda(5, 5))  # saída -> 10
print(sub_lambda(20, 15))  # saída -> 15


# filter() é uma função built in que permite filtrar elementos de uma lista ou dicionário a partir de uma condição, onde é passado como parâmetros a função a ser executada a cada iteração (a qual deve retornar True ou False) e a coleção a ser iterada.
lista_frutas = ["maçã", "pera", "banana", "morango", "uva", "melancia"]

# Irá filtrar somente as frutas que tenham um total de letras igual ou menor que 4.
def filtro_frutas(fruta):
  return len(fruta) <= 4

filter_sem_lambda = list(filter(filtro_frutas, lista_frutas))
print(filter_sem_lambda)  # saída -> ['maçã', 'pera', 'uva']

filter_com_lambda = list(filter(lambda fruta: len(fruta) <= 4, lista_frutas))
print(filter_com_lambda)  # saída -> ['maçã', 'pera', 'uva']


print("- - - - - - - - - - - - -")


# Declaração de classes.
# A função '__init__' é a função responsável por construir uma instância da classe (constructor) onde o primeiro atributo 'self' é para referenciar o pŕoprio objeto (this).
class Calculadora:

  # adição
  def soma(self, a: int, b: int):
    resultado_soma = a + b
    print("A soma é {}".format(resultado_soma))

    return resultado_soma
  
  # subtração
  def subtracao(self, a: int, b: int):
    resultado_sub = a - b
    print("A subtração é {}".format(resultado_sub))

    return resultado_sub

  # multiplicação
  def multiplicacao(self, a: int, b: int):
    resultado_multi = a * b
    print("A multiplicação é {}".format(resultado_multi))

    return resultado_multi


  # divisão
  def divisao(self, a: int, b: int):
    resultado_div = a / b 
    print("A divisão é {}".format(resultado_div))

    return resultado_div

calculadora = Calculadora()
calculadora.soma(5, 5)
calculadora.subtracao(20, 5)
calculadora.multiplicacao(10, 2)
calculadora.divisao(100, 4)


print("- - - - - - - - - - - - - -")


class Televisao:
  def __init__(self):
    self.esta_ligada = False
    self.canal = 1
  
  def power(self):
    if self.esta_ligada:
      self.esta_ligada = False
    else:
      self.esta_ligada = True
    
  def aumentar_canal(self):
    if self.canal < 30 and self.esta_ligada:
      self.canal += 1
    
  def diminuir_canal(self):
    if self.canal > 1 and self.esta_ligada:
      self.canal -= 1

televisao = Televisao()
televisao.power()
televisao.aumentar_canal()
televisao.aumentar_canal()
televisao.aumentar_canal()
televisao.diminuir_canal()
televisao.diminuir_canal()

print("A televisão está ligada?", televisao.esta_ligada)
print("Canal atual da TV:", televisao.canal)
