import socket
from threading import Thread

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create object of socket on client side
sock.connect((host, port)) # connect to the server

def send_msg():
	msg = input("Input your text: ")
	s.send(bytes(msg, "utf8")) # send message to the server

def receive_msg():
	while True:
		# receive message from server
		message = sock.recv(1024).decode()
		print("Message: ", message)

		Thread(target=send_msg).start()

def send_msg():
	msg = input("Input your text: ")
	sock.send(bytes(msg, "utf8")) # send message to the server in encode form

if __name__ == "__main__":
	receive_thread = Thread(target=receive_msg)
	receive_thread.start()
