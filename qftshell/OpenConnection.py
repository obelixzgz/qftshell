#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Shell for Microcontroller Forth in PyQt5
#
# Copyright (C) 2021 - Trustserver S. L.
#       Bruno A. Crespo: bruno@trustserver.com
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id: $
#

from ui.Ui_OpenConnection import Ui_OpenConnection
from PyQt5.QtCore import Qt,  pyqtSlot,  QFileSystemWatcher
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPortInfo

class OpenConnection (QDialog,  Ui_OpenConnection):
	def __init__(self,  parent = None, flags = Qt.WindowFlags()):
		super().__init__(parent,  flags)
		self.sPortList = {}
		self.devChange = QFileSystemWatcher(["/dev"])
		self.devChange.directoryChanged.connect(self.on_devChange_directoryChanged)
		self.setupUi(self)
		ports = QSerialPortInfo.availablePorts()
		for i in ports:
			self.serialPort.addItem(i.portName())
			self.sPortList[i.portName()] = i
		bauds = QSerialPortInfo.standardBaudRates()
		for i in bauds:
			self.speed.addItem(str(i))
		self.speed.setCurrentText("38400")
		self.flowControl.addItem(self.tr("Software Flow Control (Xon/Xoff)"),  "SOFT")
		self.flowControl.addItem(self.tr("Hardware Flow Control (RTS/CTS)"),  "HARD")
		self.flowControl.addItem(self.tr("No Flow Control"), "NONE")
		self.flowControl.setCurrentIndex(2)
		
	@pyqtSlot()
	def on_buttonBox_accepted(self):
		self.accept()
		
	@pyqtSlot()
	def on_buttonBox_rejected(self):
		self.reject()
		
	@pyqtSlot(str)
	def on_devChange_directoryChanged(self,  path):
		ports = QSerialPortInfo.availablePorts()
		text = self.serialPort.currentText()
		self.serialPort.clear()
		for i in ports:
			n = i.portName()
			self.serialPort.addItem(n)
			self.sPortList[n] = i
		if text in self.sPortList:
			self.serialPort.setCurrentText(text)
		print("Directory changed: ",  path)
		
	@pyqtSlot(str)
	def on_serialPort_currentTextChanged(self, currentText):
		print("serialPort.currentTextChanged(%s)" % (currentText))
		if not currentText in self.sPortList:
			return
		port = self.sPortList[currentText]
		
		
