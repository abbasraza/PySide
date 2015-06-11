#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Abbas Raza (abbas.raza.1707@gmail.com)

import sys

from PySide import QtGui, QtCore
from PySide.QtCore import *
from PySide.QtGui import *

def main(args):

	a = QApplication(args)

	serial = QHBoxLayout()
	ports_cb = QComboBox()
	connect = QPushButton("Connect")
	serial.addWidget(ports_cb)
	serial.addWidget(connect)

	wifi = QHBoxLayout()
	wifi1 = QVBoxLayout()
	ssidlabel = QLabel('SSID:')
	ssidlabel.setAlignment(Qt.AlignLeft)
	ssidtext = QLineEdit()
	ssidtext.setMaxLength(32)
	ssidtext.setMaximumWidth(80)
	ssidtext.setAlignment(Qt.AlignLeft)
	wifi1.addWidget(ssidlabel)
	wifi1.addWidget(ssidtext)
	wifi2 = QVBoxLayout()
	pwdlabel = QLabel('Password:')
	pwdlabel.setAlignment(Qt.AlignLeft)
	pwdtext = QLineEdit()
	pwdtext.setMaxLength(32)
	pwdtext.setMaximumWidth(80)
	pwdtext.setEchoMode(QLineEdit.Password)
	pwdtext.setAlignment(Qt.AlignLeft)
	wifi2.addWidget(pwdlabel)
	wifi2.addWidget(pwdtext)
	wifi3 = QVBoxLayout()
	setupwifi = QPushButton("Setup Wifi")
	ip = QLabel('IP: Not assigned')
	wifi3.addWidget(ip)
	wifi3.addWidget(setupwifi)

	wifi.addLayout(wifi1)
	#wifi.addStretch(1)
	wifi.addLayout(wifi2)
	wifi.addLayout(wifi3)

	comm = QVBoxLayout()
	textedit = QTextEdit()
	sendlabel = QLabel('Send Text')
	#sendlabel.setAlignment(Qt.AlignLeft)
	sendtext = QTextEdit()
	sendtext.setMaximumHeight(sendlabel.sizeHint().height() * 4)
	send = QPushButton("Send")
	comm.addWidget(textedit)
	comm.addWidget(sendlabel)
	comm.addWidget(sendtext)
	comm.addWidget(send)

	full = QVBoxLayout()
	full.addLayout(serial)
	full.addLayout(wifi)
	full.addLayout(comm)


	window =  QWidget()
	#window.setGeometry(500, 100, 300, 150)
	window.setLayout(full)
	window.show()

	r = a.exec_()
	quit()
	return r

if __name__ == "__main__":

	main(sys.argv)
