#! /usr/bin/env python

import thread
import time

def print_time (threadName, delay):
	count = 0
	while count < 10 :
		time.sleep(delay)
		count +=1 
		print "%s: %s" % (threadName , time.ctime(time.time()))
print "hello "
try :
	thread.start_new_thread( print_time, ("Thread-1", 2,))
	thread.start_new_thread( print_time, ("Thread-2", 2,))
except (KeyboardInterrupt) :
	print "Error: Unable to start thread "
#while 1 :
#	pass

