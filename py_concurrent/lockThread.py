#!/usr/bin/env python

import threading, time, os 

x = 0
y = 10000

def foo():
	global x , lock	
	for i in range(y) :
		lock.acquire()
		x -= 1
		lock.release()
def bar():
	global x , lock
	for i in range(y) :
		lock.acquire()
		x += 1 
		lock.release()

def main():
	global lock
	print " x nilai sebelum start : ",x 
	lock = threading.Lock()
	thread1 = threading.Thread(target = foo )
	thread2 = threading.Thread(target = bar )
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	
	print "x nilai sesudah start : ", x 

if ( __name__ == '__main__') :
	main()
