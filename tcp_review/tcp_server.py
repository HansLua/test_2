import socket

ser_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ser_socket.bind(('0.0.0.0',9000))
ser_socket.listen(10)

while True:
    try:
        client_socket,client_addr = ser_socket.accept()
    except:
        print("accept Error")
        client_socket.close()
        continue
    recv_data = client_socket.recv(1024).decode("utf-8")
    print(recv_data)
    client_socket.send('OK'.encode('utf-8'))
    client_socket.close()
ser_socket.close()
