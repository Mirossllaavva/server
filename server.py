import socket #підклюення модуля
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) #створення об'єкта
server_socket.bind(("localhost", 7754)) #прив'язуємо до нього IP-аресу 
server_socket.listen(1) #сервер очікує клієнта 
print("Сервер очікує клієнта") 
connection, address = server_socket.accept() #сервер приймає клієнта
print(f"Підключення клієнта: {address}"  ) 