# A manipulação de arquivos se torna bastante fácil com Python.
# A função open() permite que um arquivo seja aberto e;ou criado informando o caminho, o nome do arquivo e o modo de manipulação. Caso o caminho não seja especificado, será considerado o diretório corrente.
''' 
Algumas opções dos modos de manipulação:
    r -> somente leitura
    w -> somente escrita (exclui e cria novamente, caso o arquivo já exista)
    x -> escrita exclusiva (se o arquivo já existir, um erro será disparado)
    a -> leitura e escrita (não exclui caso o arquivo já exista)
    b -> modo binário
    t -> modo de texto

A combinação de alguns modos também é possível.
'''

arquivo = open("src/arquivos/meu_primeiro_arquivo.txt", "w")
arquivo.write("Hello World! Meu primeiro arquivo com Python. \n")

arquivo.close()


# A instrução 'with' permite simplicar o gerenciamento de recursos comuns, como o fluxo de manipulação de arquivos. é uma abordagem usada no tratamento de exceções e que torna o código mais limpo e legível.
# Através do bloco 'with' o processo de fechar o arquivo de forma automática.
with open("src/arquivos/meu_primeiro_arquivo.txt", "a") as arquivo:
  arquivo.write("\nAqui vai mais uma linha.\n")

# Abrindo o arquivo apenas em modo de leitura.
with open("src/arquivos/meu_primeiro_arquivo.txt", "r") as arquivo:
  for linha in arquivo.readlines():
    print(linha)


# Salvando um dicionário de dados em um arquivo.
usuarios = {
  "maria01": {"nome": "Maria da Silva", "idade": 25, "sexo": "feminino", "login": "maria01"},
  "pedro_1": {"nome": "Pedro do Nascimento", "idade": 23, "sexo": "masculino", "login": "pedro_1"},
  "jorge.r": {"nome": "Jorge Rodrigues", "idade": 28, "sexo": "masculino", "login": "jorge.r"},
  "teresinha": {"nome": "Teresa de Jesus", "idade": 35, "sexo": "feminino", "login": "teresinha"}
}

with open("src/arquivos/usuarios_bd.txt", "a") as arquivo:
  for chave, valor in usuarios.items():
    arquivo.write(chave + " : " + str(valor) + "\n")