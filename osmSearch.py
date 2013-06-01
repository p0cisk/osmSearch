# -*- coding: utf-8 -*-
"""
/***************************************************************************
 osmSearch
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
"""
# Import the PyQt and QGIS libraries
from qgis.core import  QGis
from osmSearchDialog import osmSearchDialog
from cacheDB import cacheDB

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
        db = cacheDB()
        db.addAutocompleteList(self.dock.autocompleteList)