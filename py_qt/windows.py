#!/usr/bin/env python

import sys
from PyQt4.QtGui import * 

def main():
	app = QApplication(sys.argv)
	window = QWidget()
	window.resize(480,360)
	window.show()
	button = QPushButton('Press me',window)
	button.move(200,200)
	button.show()
	okButton = QPushButton('&Ok')
	cancelButton = QPushButton('&Cancle')
	layout = QVBoxLayout()
	layout.addWidget(okButton)
	layout.addWidget(cancelButton)
	window.setLayout(layout)
	sys.exit(app.exec_())

if __name__ =='__main__' :
	main()
