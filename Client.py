import socket
import threading

PORT_NO=9567
IP_ADDRESS="127.0.0.1"


client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def client_send_message():
    message = input()
    client_socket.sendto(message.encode(), (IP_ADDRESS, PORT_NO))
    print("\t\t\t sent : " + message)

def client_receive_message():
    data,addr=client_socket.recvfrom(1024)
    print("received "+str(data))



while True:
    send_thread = threading.Thread(target=client_send_message())
    receive_thread = threading.Thread(target=client_receive_message())

    send_thread.start()
    receive_thread.start()