import socket 
client_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 7754))
while 1:
  command = input("Введіть запрос: ")
  client_socket.send(command.encode())
  
  print(client_socket.recv(1024).decode())
