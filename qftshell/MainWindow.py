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

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from ui.Ui_MainWindow import Ui_MainWindow

class MainWindow (QMainWindow,  Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

	def onSendAction(self,  s):
		print("Send", s)

	def onConnectAction(self, s): 
		print("Connect",  s)

	def onOpenAction(self, s):
		print("Open File",  s)
		
	@pyqtSlot(bool)
	def on_actionQuit_triggered(self,  checked):
		print("Quit! ",  checked)
		self.close()
