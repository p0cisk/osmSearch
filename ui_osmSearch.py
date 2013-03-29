# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PPociask\.qgis\python\plugins\osmSearch\ui_qsearch.ui'
#
# Created: Thu Mar 07 13:35:57 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
try:
    from qgis.gui import QgsFilterLineEdit
except:
    from utils import QgsFilterLineEdit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class QgsTreeWidget(QtGui.QTreeWidget):
    def __init(self, parent=None):
        QtGui.QTreeWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        if self.itemAt(event.pos()) is None:
            self.emit(QtCore.SIGNAL('clickedOutsideOfItems()'))
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
        self.eOutput.setRootIsDecorated(False)
        self.gridLayout.addWidget(self.eOutput, 1, 0, 1, 2)
        self.cbCenter = QtGui.QCheckBox(self.dockWidgetContents)
        self.cbCenter.setChecked(True)
        self.cbCenter.setObjectName(_fromUtf8("cbCenter"))
        self.gridLayout.addWidget(self.cbCenter, 2, 0, 1, 1)
        self.lblInfo = QtGui.QLabel(self.dockWidgetContents)
        self.lblInfo.setOpenExternalLinks(True)
        self.lblInfo.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lblInfo.setObjectName(_fromUtf8("lblInfo"))
        self.gridLayout.addWidget(self.lblInfo, 2, 1, 1, 1)
        osmSearch.setWidget(self.dockWidgetContents)

        self.retranslateUi(osmSearch)
        self.eOutput.header().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.eOutput.header().setStretchLastSection(False)
        QtCore.QObject.connect(self.eText, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.bSearch.click)
        QtCore.QMetaObject.connectSlotsByName(osmSearch)

    def retranslateUi(self, osmSearch):
        osmSearch.setWindowTitle(QtGui.QApplication.translate("osmSearch", "osmSearch", None, QtGui.QApplication.UnicodeUTF8))
        self.bSearch.setText(QtGui.QApplication.translate("osmSearch", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.eOutput.headerItem().setText(0, QtGui.QApplication.translate("osmSearch", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.eOutput.headerItem().setText(1, QtGui.QApplication.translate("osmSearch", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCenter.setText(QtGui.QApplication.translate("osmSearch", "Autocenter map canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInfo.setText(QtGui.QApplication.translate("osmSearch", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">© </span><a href=\"http://www.openstreetmap.org/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">OpenStreetMap</span></a><span style=\" font-size:8pt;\"> contributors</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

