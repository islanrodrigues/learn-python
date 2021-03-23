# Cada arquivo .py é considerado como sendo um módulo.
'''
Para que o Python reconheça um diretório como sendo um package, é preciso criar um arquivo nomeado de '__init__.py'.

Exemplo:
  nome_do_diretório/
      __init__.py
      modulo01.py
      modulo02.py
'''

# Importando (de duas maneiras diferentes) e fazendo uso das classes declaradas no diretório 'classes'.
from meu_package import televisao
import meu_package as mp  # para que essa forma funcione corretamente os módulos que deseja acessar devem estar expostos no __init__.

televisao_1 = televisao.Televisao()
calculadora_1 = mp.calculadora.Calculadora()  


'''
Diferentemente de outras linguagens (como Java, por exemplo) Python não possui método main. 
Sendo assim, para que as instruções sejam executadas somente quando um determinado módulo for executado (e não quando ele for importado) se usa a estrutua [ if __name__ == '__main__ ].
'''
if __name__ == '__main__':
  # Aqui dentro vai todo o código que não deve ser executado quando o módulo for importado por outro
  televisao_2 = televisao.Televisao()
  televisao_2.power()
  print("A TV está ligada?", televisao_2.esta_ligada)


# Fazendo a importação de apenas funções de um determinado módulo.
from meu_package.funcoes import imprime_soma, imprime_texto

imprime_texto("Hello World!")
imprime_soma(10, 15)