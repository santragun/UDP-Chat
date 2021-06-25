import threading
import socket

PORT_NO=9567
IP_ADDR="127.0.0.1"

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((IP_ADDR,PORT_NO))



def server_message_send():
    message=input()
    server_socket.sendto(message.encode(),(IP_ADDR,PORT_NO))
    print("\t\t\tsent "+message)

def server_message_receive():
    data,addr=server_socket.recvfrom(1024)
    print("received "+str(data))

while True:
       receive_thread=threading.Thread(target=server_message_receive())
       send_thread=threading.Thread(target=server_message_send())
       receive_thread.start()
       send_thread.start()
      # send_thread.
