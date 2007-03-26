#!/usr/bin/env python 
'''
Copyright (C) 2007 Justin Barca, justinbarca@gmail.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''
import inkex
import playsvg.pathshapes, playsvg.element, playsvg.document, playsvg.compshapes

class LotusFlower(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-p", "--petals",
                        action="store", type="int", 
                        dest="petals", default=12,
                        help="Number of petals")
        self.OptionParser.add_option("-r", "--radius",
                        action="store", type="float", 
                        dest="radius", default=300,
                        help="Radius of flower")
	self.OptionParser.add_option("-l", "--petallength",
                        action="store", type="float", 
                        dest="petallength", default=50.0,
                        help="Petal length")
	self.OptionParser.add_option("-c", "--controldistance",
                        action="store", type="float", 
                        dest="controldistance", default=0.5,
                        help="Distance ratio for control points")

	
	
	
    def effect(self):
        docu = playsvg.document.Document(document=self.document)
	path = playsvg.pathshapes.lotusPetalFlower(self.options.petals, self.options.radius, self.options.radius+self.options.petallength, self.options.controldistance)
	new = playsvg.element.buildPath(docu, path, {'style':'stroke:black;fill:none'})
	self.document.documentElement.appendChild(new)

e = LotusFlower()
e.affect()
