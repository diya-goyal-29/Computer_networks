import socket

def request(str) :
	if (str[0] == "GET") :
		req_str = "GET /assignment1?request={} HTTP/1.1\r\n\r\n".format(str[1])
	elif(str[0] == "PUT") :
		req_str = "PUT /assignment1/{}/{} HTTP/1.1\r\n\r\n".format(str[1], str[2])
	elif(str[0] == "DELETE") :
		req_str = "DELETE /assignment1/{} HTTP/1.1\r\n\r\n".format(str[1])
	else :
		print("Please enter correct format....")
		return
	s.send(req_str.encode())
	rmsg = s.recv(1024).decode().split(" ")
	rmsg.remove("HTTP/1.1")
	print(' '.join(rmsg))

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()

#print(dst_ip)

port = 12346

s.connect((dst_ip, port))

while(True) :
	str = raw_input().split(" ")
	if(str[0] == "-1") :
		s.send("BYE HTTP/1.1\r\n\r\n")
		break
	request(str)
s.close()
