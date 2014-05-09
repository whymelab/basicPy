#!/usr/bin/env python
import threading , time

def plus():
	global x , y 
	for i in range(y) :
		with rlock_x:
			with rlock_x:
				x+=1

def min():
	global x ,y 
	for i in range(y) :
		with rlock_x :
			with rlock_x:
				x -=1 
def main():
	global x , y, lock_x , lock_y, rlock_x
	x = 0 
	y = 10000
	rlock_x = threading.RLock()
	lock_x = threading.Lock()
	lock_y = threading.Lock()
	thread1 = threading.Thread(target=plus)
	thread2 = threading.Thread(target=min)
	thread1.start()
	thread2.start()
	thread2.join()
	thread1.join()
 	print x 	
if ( __name__ == '__main__') :
	main()
