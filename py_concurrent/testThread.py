#!/usr/bin/env python

import threading
import thread  
import time

def loop():
	global i, lock
	i = 0
	lock.acquire()	 
	try:
		while i < 2 :
			time.sleep(1) 
			print "nilai i : " , i
			#print threading.enumerate()
			#print threading.activeCount()
			#print threading.currentThread()
			print "thread is run in ", time.ctime()
			i+=1
	finally :
		lock.release()
def main():
	global i, lock
	lock = threading.Lock()
	print "Thread Main : ", threading.currentThread()
	print "Thread yang active ", threading.activeCount()
	print "=============Belum start Thread=================="
	Thread1 = threading.Thread(target=loop,name="thread-1")
	Thread2 = threading.Thread(target=loop,name="thread-2")
	Thread1.setDaemon(True)
	Thread1.isDaemon()
	Thread2.isDaemon()
	Thread1.start()
	Thread2.start()
	Thread1.join()
	Thread2.join()
	print "=============setelah start Thread================"
	print "Thread Main : ", threading.currentThread()
	print "Thread yang active ", threading.activeCount()
	

if ( __name__ == "__main__") :
	main()

