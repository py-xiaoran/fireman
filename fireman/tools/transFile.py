import socket
import os
from SocketServer import TCPServer,StreamRequestHandler
PORT = 8080

class TransRequestHandler(StreamRequestHandler):
    def handle(self):
        has_trans_dir()
        file_name = self.request.recv(1024)
        file_name = os.path.basename(file_name)
        if not file_name:
            print "get file_name is not succeed!"
            return 
        file_name = os.path.join('./trans/',file_name)
        self.request.sendall('get file name ok!\n')
        with open(file_name,"w+") as f:
            #it = iter((lambda:f.write(self.request.recv(4096))),None)  
            src = self.request.recv(4096)
            while src:
                f.write(src)   
                print "write to file:%s"%src
                src = self.request.recv(4096)
        print "complited!"

def has_trans_dir():
    if not os.path.isdir("./trans"):
        os.mkdir("./trans")

def server():
    addr = ("",PORT)
    #sock = socket.socket()
    #sock.bind(addr)
    #handel = StreamRequestHandler(request,'','')
    serv = TCPServer(addr,TransRequestHandler)
    serv.serve_forever()

if __name__ =="__main__":
    print "Quit server please enter:CTRL+C"
    server()
