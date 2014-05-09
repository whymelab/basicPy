#!/usr/bin/env python 
print "bilangan ganjil dari 0 - 100 Akan dijumlahakan semua" ;
i=0;
j=0;
while i<100 : 
	if i%2==0 :
		i+=1;
	else :
		print i ," tambah ", j 
		j=j+i;
		print "hasil nya adalah ",j
		i+=1;
print "========================================="
print "jadi hasilnya adalah : ", j
