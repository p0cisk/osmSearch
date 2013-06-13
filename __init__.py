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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "osmSearch"
def description():
    return "Search OpenStreetMap data by name or address using Nominatim service (QGIS >= 2.0 required)"
def icon():
    return "icon.png"
def classFactory(iface):
    from osmSearch import osmSearch
    return osmSearch(iface)

