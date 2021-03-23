# Importando as libs 'socket' e 'ftplib' que permitem trabalhar com o envio de dados através da rede.
# [ from <modulo> import * ] permitiria importar tudo pertencente ao módulo, eliminando a necessidade de ser feito <modulo>.<something>.
import socket
import ftplib

def identifica_ip():
  resposta = "S"

  while resposta == "S":
    url = input("Digite uma URL válida: ")
    ip = socket.gethostbyname(url)  # captura o endereço IP do host relacionado

    print("\n=== O IP referente a URL informada é:", ip)

    resposta = input("\n\nDigite <S> para continuar ou qualquer tecla para sair: ").upper()
  
  print("\n\n*** Você saiu do programa ***")


def cliente_tcp():
  servidor = "127.0.0.1"  # localhost
  porta = 43210  # informação da porta de entrada no servidor

  # Recebendo um texto através do input do usuário e convertendo para bytes com o enconde UTF-8
  msg = bytes((input("Digite alguma coisa: ")), 'utf-8')

  # AF_INET -> informa o tipo de identificação com o servidor (nesse caso, será via DNS ou IP).
  # SOCK_STREAM -> informa o tipo de comunicação (nesse caso, protocolo TCP).
  obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # O método connect() permite que o objeto socket se conecte nas informações de servidor e porta passados como parâmetro.
  obj_socket.connect((servidor, porta))

  # O método send() permite enviar uma mensagem através da conexão.
  obj_socket.send(msg)

  # O método recv() permite receber a mensagem através da conexão, informando a quantidade de bytes máximos que pode receber (1024).
  resposta = obj_socket.recv(1024)

  print("Recebemos:", resposta)

  obj_socket.close() 


def cliente_udp():
  servidor = "127.0.0.1"  # localhost
  porta = 43210  # informação da porta de entrada no servidor

  # AF_INET -> informa o tipo de identificação com o servidor (nesse caso, será via DNS ou IP).
  # SOCK_DGRAM -> informa o tipo de comunicação (nesse caso, protocolo UDP).
  obj_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # O método connect() permite que o objeto socket se conecte nas informações de servidor e porta passados como parâmetro.
  obj_socket.connect((servidor, porta))

  saida = ""

  while saida != "X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor, porta))

    dados, origem = obj_socket.recvfrom(65535)

    print("Resposta do servidor:", dados.decode())

    saida = input("\n\nDigite <X> para sair: ").upper()
  
  obj_socket.close()


def conexao_ftp_1():
  ftp = ftplib.FTP("ftp.ibiblio.org")
  print(ftp.getwelcome())

  ftp.quit()


def conexao_ftp_2():
  ftp = ftplib.FTP("ftp.ibiblio.org")
  print(ftp.getwelcome())

  usuario = input("Digite o usuário: ")
  senha = input("Digite a senha: ")

  # O método login() permite estabelecer a conexão com servidor FTP.
  ftp.login(usuario, senha)

  # O método pwd() retorna o diretório atual do ambiente conectado.
  print("Diretório atual de trabalho:", ftp.pwd())

  # O método cwd() permite a alteração do diretório atual.
  ftp.cwd('pub')
  print("Diretório corrente atualizado:", ftp.pwd())

  # O método retrlines() com o parâmetro LIST permite listar todos os arquivos dentro do direório atual.
  print(ftp.retrlines('LIST'))

  ftp.quit()


if __name__ == '__main__':
  '''
  Para estabelecer a comunicação entre os clientes e servidores, é preciso inicializar os scripts no diretório 'servidores'.
  Métodos de ação comentados (descomentar para usar). 
  '''
  # identifica_ip()
  # cliente_tcp()
  # cliente_udp()
  # conexao_ftp_1()
  # conexao_ftp_2()