import socket


recieverIP = "10.0.0.2"
recieverPort   = 1234
bufferSize  = 1024 #Message Buffer Size

# bytesToSend = str.encode(msgFromServer)

# Create a UDP socket
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to localIP and localPort
socket_udp.bind((recieverIP, recieverPort))

print("UDP socket created successfully....." )
expected_sequence = '0'
pkts = []
count = 0

while True:

    recieve_msg, address = socket_udp.recvfrom(bufferSize)
    if(recieve_msg == '1'.encode()):
    	for k in pkts:
    		file.write(k)
    	print("Transfer Completed......")
    	file.close()
    	socket_udp.close()
    	break
    required_msg = recieve_msg[16:]
    # recieve_msg = (recieve_msg)
    #print(recieve_msg)
    # print(required_msg)

    seq_num = recieve_msg[:16]
    seq_num = seq_num.decode()

    
    recieved_sequence = (seq_num[15])
    #print(required_msg)
    #print(recieved_sequence)
    #print(expected_sequence)
    file = open("recieved_file.jpg", "wb")
    if(expected_sequence == recieved_sequence) :
    	count = count + 1
    	type(required_msg)
    	pkts.append(required_msg)
    	# print("packet success.")
    	#file.write(bytes(required_msg))
    	if expected_sequence == '0' :
    		expected_sequence = '1'
    	else : 
    		expected_sequence = '0'
    	#print(expected_sequence)
    	socket_udp.sendto(recieved_sequence.encode(), address)
    # break

# print(count)