import socket 
import threading #підключення бібліотек
client_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM) #створення кліенту
client_socket.connect(("localhost", 7754)) #підключення його то локального хоста
def send_sms(): # створюмємо функціяю для відправки соо
  while 1:
    client_message = input("Введіть запрос: ") #вводимо смс
    client_socket.send(client_message.encode()) #кодуємо та відправляємо
threading.Thread(target = send_sms ).start() #створюємо поток
while 1:
  try:
    
    print("\nВідповідь від серверу", client_socket.recv(1024).decode()) #розкодуємо та виводимо повідомлення від серверу
  except:

    pass
