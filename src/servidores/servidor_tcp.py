import socket

def servidor_tcp():
  servidor = "127.0.0.1"  # localhost
  porta = 43210  # informação da porta de entrada no servidor

  # AF_INET -> informa o tipo de identificação com o servidor (nesse caso, será via DNS ou IP).
  # SOCK_STREAM -> informa o tipo de comunicação (nesse caso, protocolo TCP).
  obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # O método bind() permite setar as informações de nedereço e porta do servidor a ser criado.
  obj_socket.bind((servidor, porta))

  # O método listen() informa a quantidade de usuários permitidos a se conectarem a esse servidor simultaneamente.
  obj_socket.listen(2)

  print("Aguardando cliente ...")

  while True:
    # O método accept() impede que a próxima instrução seja executada atẽ que um usuário se conecte, tendo como retorno uma tupla com a conexão e o ID do cliente.
    con, cliente = obj_socket.accept()
    print("Conectado com:", cliente)

    while True:
      # O método recv() permite receber a mensagem através da conexão, informando a quantidade de bytes máximos que pode receber (1024).
      msg_recebida = str(con.recv(1024))
      print("Recebemos:", msg_recebida)

      # O método send() permite enviar uma mensagem através da conexão.
      msg_enviada = b'Hello World'  # o 'b' permite converter a mensagem para bytes.
      con.send(msg_enviada)

      break
  
  con.close()


if __name__ == '__main__':
  servidor_tcp()
