import socket
from threading import Thread

clients = [] # store information of connected clients

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket object
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # set configuration so that many clients can request on one single port
sock.bind((host, port)) # binds the socket with the given IP and port

def handle_clients(conn):
	while True:
		msg = conn.recv(1024)
		broadcast(msg)

# send the message to the all connected clients.
def broadcast(msg):
	for client in clients:
		client.send(msg)

def client_connection():
	while True:
		# server is accepting the connection from clients
		client_conn, client_addr = sock.accept() # accept return two things -> connection and address of the client.
		print("Client", client_conn, "has joined with address: ", client_addr)

		clients.append(client_conn)

		# setting up message from send
		message = "Welcome join the Chat Room..."
		client_conn.send(message.encode()) # send message in form of bytes

		Thread(target=handle_clients, args=(client_conn,)).start()


if __name__ == "__main__":
	# server is listening and accept users
	sock.listen(2)
	print("listening on port : ", port, "......")

	# start the accept function into thread for handle multiple request at once
	t = Thread(target=client_connection)

	t.start() # start thread
	t.join() # thread wait for main thread to exit