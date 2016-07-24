import socket
import threading

'''
if __name__ == '__main__':
    print ('plese type host IP adress:',end = '')
    host = str(input())
    port = 6000
    cSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #sSock.bind((host,port))
    #sSock.listen(10)
    print('connecting...')
    cSock.connect((host,port))
    print('connect scucesfull')

    while True:
        print('Type Message :', end='')
        s_msg = (str(input())).encode('utf-8')
        if s_msg in (b'exit',b''):
            cSock.sendall(b'exit')
            break
        cSock.sendall(s_msg)

        print('plese Wait')
        inStr = cSock.recv(1024)
        if inStr in (b'exit', b'',b'exit\n',b'exit\r\n',b'exit\r'):
            break
        print(inStr.decode('utf-8'))
    print('system exit')
    cSock.close()
'''
class Cly:
    def __init__(self,bord,port,ip):


        self.cSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stopEvent = threading.Event()
        self.bord = bord
        print('connecting...')
        self.cSock.connect((ip, port))
        print('conected')
        self.thredRecv = threading.Thread(target=self.recvWite)
        self.thredRecv.start()


    def sent(self,s_str):


        s_msg = s_str.encode('utf-8')
        if s_msg in (b'exit', b''):
            self.cSock.sendall(b'exit')
            self.exit_rcv()
        else:
            self.cSock.sendall(s_msg)

    def exit_rcv(self):
        self.stopEvent.is_set()
        self.bord.rcv('exit')
        self.cSock.close()

    def recvWite(self):
        while not self.stopEvent.is_set():
            inStr = self.cSock.recv(1024)
            if inStr in (b'exit', b'', b'exit\n', b'exit\r\n', b'exit\r'):
                self.cSock.sendall(b'exit')
                break
            self.bord.rcv(inStr.decode('utf-8'))

        self.exit_rcv()





