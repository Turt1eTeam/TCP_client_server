from base64 import encode
import socket


sock = socket.socket()
sock.connect((socket.gethostname(), 1111))
while True:
    strings=input('Введите сообщение: ')
    code = strings.encode('utf-8')
    sock.send(code)
    data = sock.recv(1024)
    print (str(data,'utf-8'),end='\n')
    if strings=='Выход':
        break
sock.close()
