#!/usr/bin/env python

import threading, time

def plus():
	global y 
	for i in range(1000) :
		semaphore.acquire()
		y+=1;
		semaphore.release()
def min():
	global y
	for i in range(1000) :
		semaphore.acquire()
		y-=1;
		semaphore.release()
def main():
	global x , y , semaphore
	x = y = 0	
	semaphore = threading.Semaphore(1)
	thread1 = threading.Thread(target=plus)
	thread2 = threading.Thread(target=min)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print y
if (__name__=='__main__'):
	main()
