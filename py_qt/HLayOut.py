#!/usr/bin/env python

from PyQt4.QtGui import * 
import sys

def main():
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.resize(640,320)
	widget.show()
	label1 = QLabel('H 1')
	label2 = QLabel('H 2')
	label3 = QLabel('H 3')
	Hlayout = QHBoxLayout()
	Hlayout.addWidget(label1)
	Hlayout.addStretch(1)
	Hlayout.addWidget(label2)
	Hlayout.addWidget(label3)
	Hlayout.addStretch(1)
	widget.setLayout(Hlayout)
	sys.exit(app.exec_())
if __name__ == '__main__' :
	main()
