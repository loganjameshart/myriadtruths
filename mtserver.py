import socket
import os
import sys

# creating constants
SYSTEM = sys.platform
USER = os.getlogin()
HOSTNAME = socket.gethostname()
HOSTADDRESS = socket.gethostbyname(HOSTNAME)


# function definitions
def username():
	'''Returns username.'''
	return os.getlogin()

def peep(directory):
	'''Returns directory as list.'''
	return os.listdir(directory)


# make listening server
server = socket.socket()
server.bind((HOSTADDRESS,6666))
server.listen(1)
print('Awaiting connection...')
conn, addr = server.accept()

# once connected, creates the interactive shell session 
if conn:
	conn.sendall(f'Welcome to the shell on {USER}'.encode())
	while True:
		if not conn:
			break
		conn.sendall(b'''
Please select a command.
		
	username		Returns username
	system			Returns system type
	peep			Asks for directory, then lists what's in it
	snatch			Asks for file path, then sends file to client
	quit			Closes connection
		
''')
		
		command = conn.recv(9999).decode()
		print(f'Executing {command}.')
		
		if 'quit' in command.lower():
			conn.sendall(b'Ending connection.\n')
			conn.close()
			break
		elif 'system' in command.lower():
			conn.sendall(f'System type is {SYSTEM}.\n'.encode())
			continue
		elif 'username' in command.lower():
			username_message = "The server's username is: " + username() + '\n'
			conn.sendall(username_message.encode())
			continue
		elif 'peep' in command.lower():
			conn.sendall(b'Where would you like to peep\n')
			directory = conn.recv(9999).decode().strip('\r\n')
			try:
				server_directory_list = peep(directory)
				for item in server_directory_list:
					conn.sendall((item + '\n').encode())
				continue
			except:
				conn.sendall(b"Couldn't find that directory. Please check the path.")
				continue
		elif 'snatch' in command.lower():
			conn.sendall(b'Please give a filename to snatch.\n')
			snatched_file = conn.recv(9999).decode().strip('\r\n')
			try:
				with open(snatched_file, 'rb') as file:
					file_data = file.read()
					conn.sendall(file_data)
				continue
			except:
				conn.sendall(b"Couldn't find file. Please check the path.")
				continue
		else:
			conn.sendall(b'\nINVALID COMMAND\n')
			continue
			
server.close()
