# -*- coding: utf-8 -*-
"""
/***************************************************************************
 osmSearchDialog
                                 A QGIS plugin
 Save notes in QGIS projects
                              -------------------
        begin                : 2012-03-31
        copyright            : (C) 2012 by Piotr Pociask
        email                : opengis84 (at) gmail (dot) com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 TODO:
 - cache results
 - autocomplete from history
 - copy results to layer
 - choose nomiantim server
"""
from PyQt4.QtCore import QObject, SIGNAL, Qt, QVariant
from PyQt4.QtGui import QTreeWidgetItem, QColor, QDockWidget
from qgis.core import QGis, QgsGeometry, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsRectangle
from qgis.gui import QgsRubberBand

import urllib, urllib2, json
from ui_osmSearch import Ui_osmSearch

class osmSearchDialog(QDockWidget , Ui_osmSearch ):
    def __init__(self,iface):
        self.iface = iface
        QDockWidget.__init__(self)
        self.setupUi(self)
        self.iface.addDockWidget(Qt.BottomDockWidgetArea,self)
        
        self.rb = QgsRubberBand(self.iface.mapCanvas(), QGis.Point)
        self.rb.setColor(QColor('red'))
        
        self.wgs84 = QgsCoordinateReferenceSystem()
        self.wgs84.createFromSrid(4326)
        self.proj = self.iface.mapCanvas().mapRenderer().destinationCrs()
        self.transform = QgsCoordinateTransform(self.wgs84, self.proj)
        
        QObject.connect(self.bSearch, SIGNAL("clicked()"),self.startSearch)
        QObject.connect(self.eOutput, SIGNAL("currentItemChanged(QTreeWidgetItem *, QTreeWidgetItem *)"),self.itemChanged)
        QObject.connect(self.eOutput, SIGNAL("clickedOutsideOfItems()"),self.itemChanged)
        QObject.connect(self.eText, SIGNAL("cleared()"),self.clearEdit)
        QObject.connect(self.iface.mapCanvas().mapRenderer(), SIGNAL("destinationSrsChanged()"),self.srsChanged)
        QObject.connect(self.iface, SIGNAL("newProjectCreated ()"),self.clearEdit)
        QObject.connect(self.iface, SIGNAL("projectRead ()"),self.clearEdit)
        QObject.connect(self.cbCenter, SIGNAL("stateChanged (int)"),self.autocenter )

    def startSearch(self):
        text = str(self.eText.text().toUtf8())
        if text == "":
            self.clearEdit()
        #url = 'http://open.mapquestapi.com/nominatim/v1/search.php'
        url = 'http://nominatim.openstreetmap.org/search'
        params = urllib.urlencode({'q': text,'format': 'json','polygon_text':'1'})
        response = json.load(urllib2.urlopen(url+'?'+params))
        self.loadData(response)

    def loadData(self, data):
        self.rb.reset(QGis.Point)
        self.eOutput.clear()
        items = []
        for d in data:
            try:
                geometry = d['geotext']
            except KeyError:
                geometry = 'POINT(%s %s)' % (d['lon'], d['lat'])
            item = QTreeWidgetItem([d['display_name'], d['type']])
            item.setData(0, Qt.UserRole, QVariant(geometry))
            items.append(item)
        self.eOutput.insertTopLevelItems(0, items)

    def itemChanged(self, current=None, previous=None):
        if current:
            wkt = str(current.data(0,Qt.UserRole).toString())
            geom = QgsGeometry.fromWkt(wkt)
            if self.proj.srsid() != 4326:
                geom.transform(self.transform)
            self.rb.setToGeometry(geom, None)
            if self.cbCenter.isChecked():
                self.moveCanvas(geom.centroid().asPoint(), self.iface.mapCanvas().extent())
        else:
            self.rb.reset(QGis.Point)
            self.eOutput.setCurrentItem(None)

    def srsChanged(self):
        self.proj = self.iface.mapCanvas().mapRenderer().destinationCrs()
        self.transform = QgsCoordinateTransform(self.wgs84, self.proj)

    def clearEdit(self):
        self.eOutput.clear()
        self.eText.clear()
        self.rb.reset(QGis.Point)

    def autocenter(self, state):
        if state and self.rb.size():
            self.moveCanvas(self.rb.asGeometry().centroid().asPoint(), self.iface.mapCanvas().extent())

    def moveCanvas(self, newCenter, oldExtent):
        newExtent = QgsRectangle(oldExtent)
        newExtent.scale(1, newCenter)
        self.iface.mapCanvas().setExtent(newExtent)
        self.iface.mapCanvas().refresh()

