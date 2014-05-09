#!/usr/bin/env python

import threading, time

def loop1():
	global x
	lock.acquire()
	for i in range(x):
		x-=1
	lock.release()

def loop2():
	global x
	lock.acquire()
	for i in range(x):
		x+=1
	lock.release()

def loop(x):
	for i in range(x):
		x-=1

def loopX(x):
	for i in range(x):
		x+=1

def main():
	global x, lock
	x = 100000
	start = time.time()
	loop(x)
	loopX(x)
	end = time.time()
	print 'Squencial time ', end - start ,'Nilai x : ',x
	lock = threading.Lock()
	x = 100000
	start = time.time()
	t1 = threading.Thread(target=loop1)
	t2 = threading.Thread(target=loop2)
	t1.start()
	t2.start()
	t2.join()
	t1.join()
	end = time.time()
	print 'Thread time ',end - start ,"Nilai x : ", x
if __name__ == '__main__' :
	main()
