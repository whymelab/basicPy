#!/usr/bin/env python

import multiprocessing

def hitung(x):
	for i in range(10000):
		x=x+i
	return x

def main():
	p = multiprocessing.Pool()
	x = p.map(hitung, range(10))
	print x

if (__name__=='__main__'):
	main()
