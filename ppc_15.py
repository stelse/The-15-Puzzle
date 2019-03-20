#!/usr/bin/env python

import socket
import re

port = 33333
ip = "90.189.132.25"

sock = socket.socket()
sock.connect((ip, port))
while True:
	matr = []
	data = sock.recv(1024) # заголовок
	print(data)
	for i in range(4):
		data = sock.recv(1024).decode('utf-8')
		data = re.findall(r'\d+', data)
		[matr.append(i) for i in data]

	j = 0
	for i in range(16):
		if (int(matr[i])):
			for k in range(i+1, 16):
				if (int(matr[k]) < int(matr[i])):
					if (int(matr[i]) != 0 and int(matr[k]) != 0):
						j += 1

	for i in range(4):
		for k in range(4):
			if (int(matr[i*4+k]) == 0):
				j = j + i + 1

	if j%2 == 0:
	        print("Yes\n")        
	        sock.send('Yes\n'.encode())
	else:
	        print("No\n")
	        sock.send('No\n'.encode())

sock.close()
