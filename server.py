from base64 import decode
from curses.ascii import islower, isupper
import socket

print(' --- Сервер запущен! --- ')
sock = socket.socket()
sock.bind(('', 1111))
sock.listen(1)
conn, addr = sock.accept()
print('   Подключение установлено с: ', addr)

while True:
    data = conn.recv(1024)
    print('Сообщение: ',data,end=' ')
    text = data.decode('utf-8')
    print(text)
    sum=b''
    for sym in text:
        if sym.islower()==True:
           sum+=sym.upper().encode('utf-8')
           sum+=sym.upper().encode('utf-8')
           
        if sym.isupper()==True:
            sum+=sym.lower().encode('utf-8')
            sum+=sym.lower().encode('utf-8')
         
    conn.send(sum)
    if (str(data,'utf-8') == 'Выход'):
        break
conn.close()