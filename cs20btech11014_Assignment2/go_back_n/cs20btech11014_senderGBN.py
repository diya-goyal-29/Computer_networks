import socket
import time

senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
pkt_size  = 800 #Message Buffer Size

reTrans = []
time_ = []

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
for j in range(5) :

	file = open('testFile.jpg', 'rb')

	packet = file.read(pkt_size)
	base = 0
	seq_num = 0
	retransmitted = 0
	N = 256
	start = time.time()

	packets = []

	while True:
		seq_len = len(str(seq_num))
		temp = ""
		for i in range(16-seq_len):
			temp += "0"
		sequence_num = temp + str(seq_num)
		sequence_num = bytes(sequence_num, "utf-8")
		seq_num += 1
		msg = b"".join([sequence_num, packet])
		packets.append(msg)
		x = file.read(pkt_size)
		if x:
			packet = x
		else:
			break
	seq_num = 0
	n = len(packets)

	while seq_num < n:
		while(seq_num < base + N and seq_num < n):
			socket_udp.sendto(packets[seq_num], recieverAddressPort)
			if base == seq_num:
				socket_udp.settimeout(0.02)
			seq_num += 1
		while (base < seq_num) :
			try:
				msg_recieved, addr = socket_udp.recvfrom(pkt_size)
				msg_recieved = msg_recieved.decode()
				if msg_recieved :
					#print("acknowledgement received : ", msg_recieved)
					base = int(msg_recieved) + 1
			except:
				retransmitted += 1
				socket_udp.settimeout(0.02)
				seq_num = base
	end = time.time()
	reTrans.append(retransmitted)
	time_.append(1144/(end-start))

print("average retransmissions = ", sum(reTrans)/len(reTrans), " average time = ", sum(time_)/ len(time_))

msg = "1"
socket_udp.sendto(msg.encode(),recieverAddressPort)
socket_udp.close()
file.close()