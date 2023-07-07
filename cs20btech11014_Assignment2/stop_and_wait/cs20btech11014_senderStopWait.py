import socket
import sys
import time

recieverAddressPort = ("10.0.0.2", 1234)
senderIP = "10.0.0.1"
senderPort   = 1234
pkt_size  = 800 #Message Buffer Size

reTrans = []
time_ = []

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
for j in range(5) : 
	file = open('testFile.jpg', "rb")

	packet = file.read(pkt_size)
	#print(packet)

	i = 0
	retransmitted = 0
	start = time.time()
	# count  = 0

	# j = 0
	while True:
		# print(j, end=' ')
		# j = j+1
		# print(packet)
		sequence_num = "000000000000000" + str(i)
		sequence_num = bytes(sequence_num, "utf-8")
		# print('length = ', len(sequence_num))
		# msg = sequence_num + packet
		# msg = bytes(msg, "utf-8")
		msg = b''.join([sequence_num, packet])
		# print(type(msg))
		#print(msg)
		if(socket_udp.sendto(msg,recieverAddressPort)):
			# print("msg sent")
			# count = count + 1
			while True:
				try:
					socket_udp.settimeout(0.1)
					msg_recieved, addr = socket_udp.recvfrom(pkt_size)
					msg_recieved = msg_recieved.decode()
					#print(msg_recieved)
					if(msg_recieved == str(i)) :
						break
				except: 
					socket_udp.sendto(msg,recieverAddressPort)
					retransmitted = retransmitted + 1

			x = file.read(pkt_size)
			if x:
				packet = x
			else:
				break
			if(i == 0) : 
				i = 1
			else : 
				i = 0

	end = time.time()
	reTrans.append(retransmitted)
	time_.append(1144/(end-start))

print("average retransmissions = ", sum(reTrans)/len(reTrans), " average throughput = ", sum(time_)/ len(time_))

msg = "1"
socket_udp.sendto(msg.encode(),recieverAddressPort)
socket_udp.close()
file.close()
# print(count)