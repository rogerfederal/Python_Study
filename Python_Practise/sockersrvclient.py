import socket
client = socket.socket()
client.connect(('techinfo.xin',9999))
while True:
    msg = input(">>>").strip()
    if len(msg) ==0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(8092)
    print("recv:>",data.decode())
client.close()