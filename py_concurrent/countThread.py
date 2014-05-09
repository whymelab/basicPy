#!/usr/bin/env python

import threading
import time
import os

def Threadnya(number , name) :
	x=0 
	print "x = " , x
	while x < number:
		print "==> diwaktu ke ", time.ctime(),"| thread : ",name,"| x : ",x
		time.sleep(1)
		x+=1

def main():
	print "cetak Thread "
	thread1 = threading.Thread(target=Threadnya, args=(10,'Thread 1'))
	thread2 = threading.Thread(target=Threadnya, args=(20,'Thread 2'))
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

		
if ( __name__ == '__main__' ):
	main()
