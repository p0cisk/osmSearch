# -*- coding: utf-8 -*-
"""
/***************************************************************************
 osmSearch
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
"""
# Import the PyQt and QGIS libraries
from qgis.core import  QGis
from osmSearchDialog import osmSearchDialog

"""
TODO:
-limit search to visible area (checkbox)
-handle error when tranfomration failed
-lepsza wizualizacja wynikow, moZe rozwijane dane adresowe
-select search: nominatim & mapquest
-dopracowac strukture wtyczki, zeby latwiej bylo ewentualnie dodawac nowe silniki wyszukiwania (geonames?)
-cache data (decorator)
"""

class osmSearch:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        self.dock  = osmSearchDialog(self.iface)

    def unload(self):
        self.iface.removeDockWidget(self.dock)
        self.dock.rb.reset(QGis.Point)
        del self.dock.rb