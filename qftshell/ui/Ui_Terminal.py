# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bruno/proyectos/github/qftshell/qftshell/ui/Terminal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(900, 560)
        self.verticalLayout = QtWidgets.QVBoxLayout(Terminal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Terminal)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.input = Qsci.QsciScintilla(self.splitter)
        self.input.setToolTip("")
        self.input.setWhatsThis("")
        self.input.setObjectName("input")
        self.output = Qsci.QsciScintilla(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setBaseSize(QtCore.QSize(0, 200))
        self.output.setToolTip("")
        self.output.setWhatsThis("")
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "Form"))
from PyQt5 import Qsci


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Terminal = QtWidgets.QWidget()
    ui = Ui_Terminal()
    ui.setupUi(Terminal)
    Terminal.show()
    sys.exit(app.exec_())
