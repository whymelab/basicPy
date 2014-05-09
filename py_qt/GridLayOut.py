#!/usr/bin/env python

import sys
from PyQt4.QtGui import *

def main():
	App = QApplication(sys.argv)
	Widget = QWidget()
	Widget.setWindowTitle('Hello Grid Layout')
	Widget.resize(640,640)
	NameLabel = QLabel('Name : ')
	NameEdit = QLineEdit()
	addressLabel = QLabel('Address : ')
	addressEdit = QTextEdit()
	"""
	L1 = QLabel('H1')
	L2 = QLabel('H2')
	L3 = QLabel('H3')	
	L4 = QLabel('H4')
	L5 = QLabel('H5')
	L6 = QLabel('H6')
	L7 = QLabel('H7')
	L8 = QLabel('H8')
	L9 = QLabel('H9')
	print 'Masuk QGridLayout'
	"""
	GLayout = QGridLayout()
	"""
	QL = [L1,L2,L3,L4,L5,L6,L7,L8,L9]
	i=j = z = 0
	A = True
	while A :
		for i in range(2):
			for j in range(2) :
				GLayout.addWidget(QL[z],i,j)
				z+=1
				print 'i : ',i,'j : ',j,'z : ',z
				if z == 6 :
					A = False
				
	print 'Tampil GridLayout'
	"""
	GLayout.addWidget(NameLabel,0,0)
	GLayout.addWidget(NameEdit,0,1)
	GLayout.addWidget(addressLabel,1,0)
	GLayout.addWidget(addressEdit,1,1)
	Widget.setLayout(GLayout)
	Widget.show()
	sys.exit(App.exec_())	

if __name__ == '__main__' :
	main()
