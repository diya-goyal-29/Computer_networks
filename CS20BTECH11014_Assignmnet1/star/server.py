import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).

key_value = dict()
dst_ip = "10.0.1.3"#str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12345

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

c, addr = s.accept()
print ('Got connection from', addr )

while True:
	recvmsg = c.recv(1024).decode()
	if(recvmsg == "BYE HTTP/1.1"):
		print("Server connection closed...")
  		c.close()
  		break
	print('Server received ' + recvmsg)
	msg = recvmsg.split(" ")
	mtd = msg[0]
	if(mtd == "GET"):
		str = msg[1].split("=")
		key = str[1]
		if (key in key_value):
			smsg = "HTTP/1.1 " + key_value[key]
		else:
			smsg = "HTTP/1.1 ERROR 120 Key is not present..."
	if(mtd == "PUT"):
		str_ = msg[1].split("/")
		if(str_[2] in key_value):
			smsg = "HTTP/1.1 Value updated..."
			key_value[str(str_[2])] = str(str_[3])
			print(key_value)
		else :
			smsg = "HTTP/1.1 Value added..."
			key_value[str_[2]] = str_[3]
			print(key_value)
	smsg = smsg + "\r\n\r\n"
	c.send(smsg.encode())