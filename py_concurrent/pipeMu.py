#!/usr/bin/env python

import multiprocessing, time

def cons(connect1 , connect2):
	connect2.close()
	while True:
		try: 
			item = connect1.recv()
			#item1 = connect1.recv()
			connect1.send(item)
		except EOFError:
			break
		print item 

def pro(data, connect):
	for item in data:
		connect.send(item)	
		recv =connect.recv()
		print "---> ",recv
	
	#for item in range(1000):
	#	connect2.send(item)

def main():
	p1, p2 = multiprocessing.Pipe()
	coniis = multiprocessing.Process(target=cons, args=(p1,p2))
	coniis.start()
	p1.close()
	print "telah membuat Process"	
	se = xrange(100)
	pro(se, p2)
	p2.close()
	#p2.close()

if (__name__=='__main__'):
	main()
