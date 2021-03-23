import socket

def servidor_udp():
  servidor = "127.0.0.1"  # localhost
  porta = 43210  # informação da porta de entrada no servidor

  # AF_INET -> informa o tipo de identificação com o servidor (nesse caso, será via DNS ou IP).
  # SOCK_DGRAM -> informa o tipo de comunicação (nesse caso, protocolo UDP).
  obj_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # O método bind() permite setar as informações de nedereço e porta do servidor a ser criado.
  obj_socket.bind((servidor, porta))

  print("Servidor pronto ...")

  while True:
    # limitando o tamanho de dados docliente (tamanho máximo permitido)
    dados, origem = obj_socket.recvfrom(65535)

    print("Origem:", origem)
    print("Dados recebidos:", dados.decode())

    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

  obj_socket.close()


if __name__ == '__main__':
  servidor_udp()