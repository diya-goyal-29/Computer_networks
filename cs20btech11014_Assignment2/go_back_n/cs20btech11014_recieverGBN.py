import socket

recieverIP = "10.0.0.2"
recieverPort   = 20002
bufferSize  = 1024 #Message Buffer Size

# bytesToSend = str.encode(msgFromServer)

# Create a UDP socket
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to localIP and localPort
socket_udp.bind((recieverIP, recieverPort))

print("UDP socket created successfully....." )

seq_num = 0
pkts = []


file = open("recieved_image.jpg", "wb")

while True:
	recieve_msg, address = socket_udp.recvfrom(bufferSize)
	if(recieve_msg == '1'.encode()):
		for k in pkts:
			file.write(k)
			#print("Transfer Completed......")
		file.close()
		socket_udp.close()
		break
	required_msg = recieve_msg[16:]
	rseq_num = recieve_msg[:16]
	rseq_num = rseq_num.decode()
	rseq_num = int(rseq_num)
	if seq_num == rseq_num:
		pkts.append(required_msg)
		acknowledgement_num = str(rseq_num)
		socket_udp.sendto(acknowledgement_num.encode(), address)
		seq_num += 1
	else:
		acknowledgement_num = str(seq_num-1)
		socket_udp.sendto(acknowledgement_num.encode(), address)


print("Transfer of file is successful......")
    