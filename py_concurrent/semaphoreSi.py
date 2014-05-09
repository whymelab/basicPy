#!/usr/bin/env python

import threading, time

def foo():
	global sema
	print "acquire semaphore"
	sema.acquire()
	time.sleep(10)
	print "Lanjut sema.acquire()"

def bar():
	global sema
	print "release semaphore"
	sema.release()
	print "Lanjut sema.release()"

def main():
	global sema, x 
	sema = threading.Semaphore(0) 
	thread1 = threading.Thread(target=foo)
	thread2 = threading.Thread(target=bar)
	thread2.start()
	thread1.start()
	thread1.join()
	thread2.join()

if (__name__=='__main__'):
	main()
