#!/usr/bin/env python

import threading, time 

def bar():
	global x, event_x
	while x < 10 :
		time.sleep(1)
		print 'nilai bar ',x
		x+=1
	event_x.set()	
	
def foo():
	global x, event_x
	print "Wait signal from bar "
	event_x.wait()	
	print "signal diteriam ",x

def clear():
	global x , y
	time.sleep(2)
	print "jia event diset akan di clearkan "
	if event_x.isSet() :
		event_x.clear()
	

def main():
	global x, y, event_x
	x = 0
	y = 1000
	event_x = threading.Event()
	thread1 = threading.Thread(target=bar )
	thread2 = threading.Thread(target=foo )
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

if (__name__=='__main__'):
	main()
