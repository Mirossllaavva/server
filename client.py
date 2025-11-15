import socket 
import threading 
client_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 7754))
def send_sms():
  while 1:
    client_message = input("Введіть запрос: ")
    client_socket.send(client_message.encode())
threading.Thread(target = send_sms ).start()
while 1:
  try:
    
    print("\nВідповідь від серверу", client_socket.recv(1024).decode())
  except:
    pass