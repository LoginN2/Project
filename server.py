import socket
import requests

API_KEY = ""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
server_socket.bind(server_address)
server_socket.listen(1)
print('Сервер запущен на {}:{}'.format(*server_address))
while True:
    print('Ожидание соединения...')
    connection, client_address = server_socket.accept()