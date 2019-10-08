import socket

target_host = "www.google.com"
target_port = 80

#SOCKET
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data

client.sendto(b"ABC",(target_host,target_port))

data, addr = client.recvfrom(4096)

print(data)