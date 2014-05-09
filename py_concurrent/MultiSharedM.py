#!/usr/bin/env python

import multiprocessing , random

def loop1(v,a,l):
	print v ,"========================="
	#v.value = 2.111
	l.acquire()
	for i in range(5):
		a[5+i] = i	
		print v,"->" , a[i]
	l.release()
def loop2(v,a,l):
	print v ,"========================="
	#v.value = 1.111
	l.acquire()
	for i in range(5):
		a[i] = 10*i	
		print v ,"->",a[i]
	l.release()
def main():
	i = multiprocessing.Lock()
	val = multiprocessing.Value('d', 0.0)
	arr = multiprocessing.Array('i', range(10))
	process1 = multiprocessing.Process(target=loop1, args=("process1", arr, i))
	process2 = multiprocessing.Process(target=loop2, args=("Process2", arr, i))
	process1.start()
	process2.start()
	process1.join()
	process2.join()
	print arr[:]
	#print val.value
if (__name__=='__main__'):
	main()
