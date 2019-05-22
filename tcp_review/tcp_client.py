import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',9000))

client_socket.send('see you,server'.encode('utf-8'))
ser_msg = client_socket.recv(1024)
print(ser_msg.decode())
client_socket.close()