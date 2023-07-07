import socket

def request(str) :
	if (str[0] == "GET") :
		req_str = "GET /assignment1?request={} HTTP/1.1\r\n\r\n".format(str[1])
	elif(str[0] == "PUT") :
		req_str = "PUT /assignment1/{}/{} HTTP/1.1\r\n\r\n".format(str[1], str[2])
	else :
		print("Please enter correct format....")
		return
	s.send(req_str.encode())
	rmsg = s.recv(1024).decode().split(" ")
	rmsg.remove("HTTP/1.1")
	print(' '.join(rmsg))

serverIP = "10.0.1.2"

dst_ip = "10.0.1.2"#str(input("Enter dstIP: "))
s = socket.socket()

#print(dst_ip)

port = 12346

s.connect((dst_ip, port))

# for i in range(1,7):
# 	req = ['PUT', 'key'+str(i), 'val'+str(i)]
# 	request(req)
# for j in range(1,4) :
# 	for i in range(1,7):
# 		req = ['GET', 'key'+str(i)]
# 		request(req)

while(True) :
	str = raw_input().split(" ")
	if(str[0] == "-1") :
		s.send("BYE HTTP/1.1\r\n\r\n".encode())
		break
	request(str)

s.close()