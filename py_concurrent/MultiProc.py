#!/usr/bin/env python

import multiprocessing, time
import threading
def loop1(): 
	global x, lock
	for i in range(x) :
		x-=1
def loop2():
	global x, lock
  	for i in range(x):
		x+=1
if __name__ == '__main__' :
	global x, lock 
	x = 10000000
	start = time.time()
	p1 = multiprocessing.Process(target=loop1)
	p2 = multiprocessing.Process(target=loop2)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	end = time.time()
	print end-start, "nilai x : ",x
