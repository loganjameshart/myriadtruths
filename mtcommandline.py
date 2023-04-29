import argparse
import socket
import subprocess
import os
import sys

def username():
	'''Returns username.'''
	print(os.getlogin())

def peep():
	'''Peeps directory.'''
	print(os.listdir())

### need to add user's name and original filepath to get to work ###
def change():
	'''Changes current working directory.'''
	directory = input("Please input directory to change to: ")
	os.chdir(directory)
	print(os.getcwd())
	
def snatch(file_location: str):
	'''Grabs a file from server and saves it to client's machine.'''
	
	with open(file_location,'rb') as target_file:
		data = target_file.read()
		with socket.socket() as s:
			s.connect(('',6666))
			s.sendall(data)

# makes the menu and headers
menu = argparse.ArgumentParser(
			prog="Myriad Truths - Server",
			description="Remote shell access via Python.",
			epilog="All will be revealed."
			)
# make the command line menu options
menu.add_argument('-u', help="Returns username.")
menu.add_argument('-p', help="Activates directory peep protocol.")
menu.add_argument('-s', help="Activates file snatcher protocol.")
menu.add_argument('-c', help="Activates directory changing protocol.")

args = menu.parse_args()

if args.u:
	print("Username is:\n")
	username()

if args.p:
	print('Peeping directory...')
	peep()
	
elif args.c:
	change()

elif args.s:
	print('Grabbing file...')
