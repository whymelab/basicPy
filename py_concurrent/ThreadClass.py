#!/usr/bin/env python

import threading , os , time

class Threadnya(threading.Thread):
	def __init__(self, nama , count ):
		threading.Thread.__init__(self)
		self.nama = nama 
		self.count = count 
	def run(self):
		i=0
		while i <= self.count :
			print "time : ",time.ctime(),"Thread : ",self.name," i : ",i
			i += 1
			time.sleep(1)
	
		return

def main():
	t1 = Threadnya('Thread-1',10)
	t2 = Threadnya('Thread-2',20)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

if ( __name__ == '__main__' ):
	main() 
		
