#!/usr/bin/env python

import multiprocessing 


def loop1(lock,x,q):
	#lock.acquire()
	for i in xrange(10):
		x+=1
		q.put(i)
	#lock.release()
	print "di looping 1", x

def loop2(lock,x,q):
	#lock.acquire()
	for i in xrange(10):
		x-=1
		q.put(i)
	#lock.release()
	print "di looping 2",x 
def main():
	x = 0
	queue = multiprocessing.Queue()
	lock = multiprocessing.Lock()
	process1 = multiprocessing.Process(target=loop1,args=(lock,x,queue))
	process2 = multiprocessing.Process(target=loop2,args=(lock,x,queue))
	process1.start()
	process2.start()
	process2.join()
	process1.join()
	for i in xrange(20):
		print queue.get()
if (__name__=='__main__'):
	main()
