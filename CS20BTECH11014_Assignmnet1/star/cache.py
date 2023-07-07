import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).

key_value = dict()
dst_ip = "10.0.1.3"#str(input("Enter Server IP: "))

s1 = socket.socket()
print ("Socket 1 successfully created")
s2 = socket.socket()
print ("Socket 2 successfully created")

dport1 = 12346
dport2 = 12345

s1.bind(("10.0.1.2", dport1))
print ("socket 1 binded to %s" %(dport1))


s1.listen(5)
print ("socket 1 is listening")
s2.connect((dst_ip, dport2))


c, addr = s1.accept()
print ('Got connection from', addr )

while True:
	recvmsg = c.recv(1024).decode()
	if(recvmsg == "BYE HTTP/1.1"):
		print("Cache connection closed...")
  		c.close()
  		s2.send("BYE HTTP/1.1\r\n\r\n".encode())
  		break
	print('Cache received ' + recvmsg)
	msg = recvmsg.split(" ")
	mtd = msg[0]
	if(mtd == "GET"):
		str = msg[1].split("=")
		key = str[1]
		if (key in key_value):
			smsg = "HTTP/1.1 " + key_value[key]
		else:
			s2.send(recvmsg.encode())
			smsg = s2.recv(1024).decode()
			m = smsg.split(" ")
			key_value[key] = m[1]
			# smsg = "HTTP/1.1 ERROR 120 Key is not present..."
	if(mtd == "PUT"):
		s2.send(recvmsg.encode())
		smsg = s2.recv(1024).decode()
		print(smsg)
	smsg = smsg + "\r\n\r\n"
	c.send(smsg.encode())

s2.close()