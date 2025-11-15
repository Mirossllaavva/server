import socket #підклюення модуля
import threading 
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) #створення об'єкта
server_socket.bind(("localhost", 7754)) #прив'язуємо до певної адреси в інтернеті(хост)
connect_client = []
server_socket.listen(5) #сервер очікує клієнта 
server_socket.setblocking(0)
print("Сервер очікує клієнта") 
def send_sms(message):
    for connect in connect_client:
        try:
            connect.send(message.encode())
        except:
            pass


def accept_sms():
    while 1:
        try:
            for connect in connect_client:
                message = connect.recv(1024).decode()
                if message:
                    print(f"Запрос кліента: {message}")
                    send_sms(message)
                # server_sms = input("Введіть відповідь: ")
                # connect.send(server_sms.encode())


        except: 
            pass
threading.Thread(target=accept_sms).start()
# def send_sms():
#     while 1:
#         server_sms = input("Введіть відповідь: ")
#         server_socket.send(server_sms.encode())
# threading.Thread(target = send_sms).start()
while 1:
    try:
        
        connection, address = server_socket.accept()
        connection.setblocking(0)
        connect_client.append(connection)
        print(f"Підключення клієнта: {address}"  ) 
    except:
        pass
# while 1:
#     try:
#         command = connection.recv(1024).decode()
#         if command == "2 + 2":
#             connection.send("4".encode())
        
#     except:
#         pass
