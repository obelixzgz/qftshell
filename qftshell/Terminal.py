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

from ui.Ui_Terminal import Ui_Terminal
from PyQt5.QtCore import Qt,  pyqtSlot,  QFileSystemWatcher
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSerialPort import QSerialPortInfo

class Terminal (QWidget,  Ui_Terminal):
	def __init__(self,  parent = None, flags = Qt.WindowFlags()):
		super().__init__(parent,  flags)
		self.setupUi(self)
