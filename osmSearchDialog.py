﻿# -*- coding: utf-8 -*-
"""
/***************************************************************************
 osmSearchDialog
                                 A QGIS plugin
 Search OpenStreetMap data by name or address using Nominating service
                              -------------------
        begin                : 2013-03-29
        copyright            : (C) 2013 by Piotr Pociask
        email                : piotr.pociask (at) gis-support (dot) pl
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
 - copy results to layer
 - choose nomiantim server
 - limit search to visible area
"""
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTreeWidgetItem, QColor, QDockWidget, QMessageBox, QCompleter
from qgis.core import QGis, QgsGeometry, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsRectangle, QgsApplication
from qgis.gui import QgsRubberBand, QgsMessageBar

import urllib, urllib2, json
from ui_osmSearch import Ui_osmSearch
from cacheDB import cacheDB

class osmSearchDialog(QDockWidget , Ui_osmSearch ):
    def __init__(self,iface):
        self.iface = iface
        QDockWidget.__init__(self)
        self.setupUi(self)
        self.iface.addDockWidget(Qt.BottomDockWidgetArea,self)
        self.canvas = self.iface.mapCanvas()
        
        self.rb = QgsRubberBand(self.canvas, QGis.Point)
        self.rb.setColor(QColor( 255, 0, 0, 150 ))
        self.searchCacheLimit = 1000
        
        self.wgs84 = QgsCoordinateReferenceSystem()
        self.wgs84.createFromSrid(4326)
        self.proj = self.canvas.mapRenderer().destinationCrs()
        self.transform = QgsCoordinateTransform(self.wgs84, self.proj)
        
        self.bSearch.clicked.connect(self.startSearch)
        self.eOutput.currentItemChanged.connect(self.itemChanged)
        self.eOutput.clickedOutsideOfItems.connect(self.itemChanged)
        self.eText.cleared.connect(self.clearEdit)
        self.canvas.mapRenderer().destinationSrsChanged.connect(self.crsChanged)
        self.iface.newProjectCreated.connect(self.clearEdit)
        self.iface.projectRead.connect(self.clearEdit)
        self.cbCenter.stateChanged.connect(self.autocenter)
        
        db = cacheDB()
        self.autocompleteList = db.getAutocompleteList()
        db.closeConnection()
        self.completer = QCompleter(self.autocompleteList)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.eText.setCompleter(self.completer)

    def startSearch(self):
        text = self.eText.text().encode('utf-8')
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
            item.setData(0, Qt.UserRole, geometry)
            if geometry.lower().startswith('point'):
                item.setIcon(0, QgsApplication.getThemeIcon('/mIconPointLayer.svg'))
            elif geometry.lower().startswith('linestring'):
                item.setIcon(0, QgsApplication.getThemeIcon('/mIconLineLayer.svg'))
            elif geometry.lower().startswith('polygon'):
                item.setIcon(0, QgsApplication.getThemeIcon('/mIconPolygonLayer.svg'))
            items.append(item)
        if items:
            self.eOutput.insertTopLevelItems(0, items)
            self.addSearchTerm(unicode(self.eText.text().lower()))
            
        else:
            self.iface.messageBar().pushMessage('Nothing was found!', QgsMessageBar.CRITICAL, 2)

    def itemChanged(self, current=None, previous=None):
        if current:
            wkt = str(current.data(0,Qt.UserRole))
            geom = QgsGeometry.fromWkt(wkt)
            if self.proj.srsid() != 4326:
                try:
                    geom.transform(self.transform)
                except:
                    self.iface.messageBar().pushMessage('CRS transformation error!', QgsMessageBar.CRITICAL, 2)
                    self.rb.reset(QGis.Point)
                    return
            self.rb.setToGeometry(geom, None)
            if self.cbCenter.isChecked():
                self.moveCanvas(geom.centroid().asPoint(), self.canvas.extent())
        else:
            self.rb.reset(QGis.Point)
            self.eOutput.setCurrentItem(None)

    def crsChanged(self):
        self.proj = self.canvas.mapRenderer().destinationCrs()
        self.transform = QgsCoordinateTransform(self.wgs84, self.proj)

    def clearEdit(self):
        self.eOutput.clear()
        self.eText.clear()
        if hasattr(self, 'rb'):
            self.rb.reset(QGis.Point)
    
    def setCompleter(self):
        self.completer.model().setStringList(self.autocompleteList)
    
    def addSearchTerm(self, text):
        if not text in self.autocompleteList:
            self.autocompleteList.append(text)
            self.setCompleter()
        while len(self.autocompleteList) > self.searchCacheLimit:
            self.autocompleteList.pop(0)

    def autocenter(self, state):
        if state and self.rb.size():
            self.moveCanvas(self.rb.asGeometry().centroid().asPoint(), self.canvas.extent())

    def moveCanvas(self, newCenter, oldExtent):
        newExtent = QgsRectangle(oldExtent)
        newExtent.scale(1, newCenter)
        self.canvas.setExtent(newExtent)
        self.canvas.refresh()