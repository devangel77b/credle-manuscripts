sock=socket.socket #create a UDP socket
locaddr= (host, port)
sock.bind(locaddr)
message = msg.encode(encoding="utf-8") #encode your command
sock.sendto(message,tello_address) #send command to tello)
