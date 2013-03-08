# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PPociask\.qgis\python\plugins\osmSearch\ui_qsearch.ui'
#
# Created: Thu Mar 07 13:35:57 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis.gui import QgsFilterLineEdit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class QgsTreeWidget(QtGui.QTreeWidget):
    def __init(self, parent=None):
        QtGui.QTreeWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        self.clearSelection()
        QtGui.QTreeView.mousePressEvent(self, event)

class Ui_osmSearch(object):
    def setupUi(self, osmSearch):
        osmSearch.setObjectName(_fromUtf8("osmSearch"))
        osmSearch.resize(634, 167)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.eText = QgsFilterLineEdit(self.dockWidgetContents)
        self.eText.setObjectName(_fromUtf8("eText"))
        self.gridLayout.addWidget(self.eText, 0, 0, 1, 1)
        self.bSearch = QtGui.QPushButton(self.dockWidgetContents)
        self.bSearch.setObjectName(_fromUtf8("bSearch"))
        self.gridLayout.addWidget(self.bSearch, 0, 1, 1, 1)
        self.eOutput = QgsTreeWidget(self.dockWidgetContents)
        self.eOutput.setObjectName(_fromUtf8("eOutput"))
        self.gridLayout.addWidget(self.eOutput, 1, 0, 1, 2)
        self.cbCenter = QtGui.QCheckBox(self.dockWidgetContents)
        self.cbCenter.setChecked(True)
        self.cbCenter.setObjectName(_fromUtf8("cbCenter"))
        self.gridLayout.addWidget(self.cbCenter, 2, 0, 1, 1)
        osmSearch.setWidget(self.dockWidgetContents)

        self.retranslateUi(osmSearch)
        QtCore.QObject.connect(self.eText, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.bSearch.click)
        QtCore.QMetaObject.connectSlotsByName(osmSearch)

    def retranslateUi(self, osmSearch):
        osmSearch.setWindowTitle(QtGui.QApplication.translate("osmSearch", "osmSearch", None, QtGui.QApplication.UnicodeUTF8))
        self.bSearch.setText(QtGui.QApplication.translate("osmSearch", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.eOutput.headerItem().setText(0, QtGui.QApplication.translate("osmSearch", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.eOutput.headerItem().setText(1, QtGui.QApplication.translate("osmSearch", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.eOutput.headerItem().setText(2, QtGui.QApplication.translate("osmSearch", "Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCenter.setText(QtGui.QApplication.translate("osmSearch", "Autocenter map canvas", None, QtGui.QApplication.UnicodeUTF8))

