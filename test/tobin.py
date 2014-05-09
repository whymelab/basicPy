#! /usr/bin/env python

def nilai(val):
	i = 1
	z = 0
	hasil = 0
	array = []
	index = []
	while val:
		index.append(i)
		array.append(val%2)
		print i,"ke :",array[z]
		hasil = hasil + array[z]*i
		i*=2
		z+=1
		val = val / 2
	array.reverse();
	index.reverse();
	print "anda memasukan : ",hasil
	print array

val=raw_input("Masukan nilai'nya : ")
x = int(val)
nilai(x)

