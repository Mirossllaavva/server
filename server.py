import socket
server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 7754))
server_socket.listen(1)
print("Сервер очікує клієнта")
connection, address = server_socket.accept()
print(f"Підключення клієнта: {address}"  )