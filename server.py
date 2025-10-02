import socket #підклюення модуля
import threading 
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) #створення об'єкта
server_socket.bind(("localhost", 7754)) #прив'язуємо до певної адреси в інтернеті(хост)
connect_client = []
server_socket.listen(5) #сервер очікує клієнта 
server_socket.setblocking(0)
print("Сервер очікує клієнта") 
def accept_sms():
    while 1:
        try:
            for client in connect_client:
                message = client.recv(1024).decode()
                print(message)
        except: 
            pass
threading.Thread(target=accept_sms).start()

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
