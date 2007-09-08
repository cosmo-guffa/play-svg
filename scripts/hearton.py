from playsvg.document import *
from playsvg.element import *
from playsvg.path import *
import playsvg.pathshapes
import os
import string


def recursiveMagenStar(docu, radius, levels):
    starGroup = docu.makeGroup()
 
    for i in range(1, levels+1):
        triPath = PathData().moveTo(Point().polerInit(float(i)/levels*radius, 0)).lineTo(Point().polerInit(float(i)/levels*radius, 1.0/3)).lineTo(Point().polerInit(float(i)/levels*radius, 2.0/3)).lineTo(Point().polerInit(float(i)/levels*radius, 0))\
        .moveTo(Point().polerInit(float(i)/levels*radius, 1.0/6)).lineTo(Point().polerInit(float(i)/levels*radius, 1.0/2)).lineTo(Point().polerInit(float(i)/levels*radius, 5.0/6)).closePath()
        starGroup.appendChild(buildPath(docu, triPath, {'style':'stroke:black; fill:none'}))
    return starGroup
docu = document.Document()
docu.appendElement( recursiveMagenStar(docu,200, 6 ))

docu.writeSVG("recursiveMagenStar.svg" )
print "done"


