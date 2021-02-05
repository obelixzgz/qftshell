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

from PyQt5.QtWidgets import QMainWindow,  QToolBar,  QAction,  QStatusBar
from PyQt5.QtGui import QIcon

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Qt Shell for Forth")
        
        toolbar = QToolBar("Forth Toolbar")
        
        actSend = QAction(QIcon("icons/arrow-curve.png"), "Send",  self)
        actSend.setStatusTip("Send actual line")
        actSend.triggered.connect(self.onSendAction)
        
        actConnect = QAction(QIcon("icons/socket.png"), "Connect",  self)
        actConnect.setStatusTip("Connect to microcontroller")
        actConnect.triggered.connect(self.onConnectAction)

        actOpen = QAction("&Open File",  self)
        actOpen.setStatusTip("Open file")
        actOpen.triggered.connect(self.onOpenAction)
        
        self.addToolBar(toolbar)
        toolbar.addAction(actConnect)
        toolbar.addAction(actSend)
        
        menu = self.menuBar()
        
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(actOpen)
        fileMenu.addAction(actConnect)

        self.setStatusBar(QStatusBar(self))
        
    def onSendAction(self,  s):
        print("Send", s)
        
    def onConnectAction(self, s): 
        print("Connect",  s)
        
    def onOpenAction(self, s):
        print("Open File",  s)
