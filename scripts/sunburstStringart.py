from playsvg.document import *
from playsvg.element import *
from playsvg.path import *
import playsvg.pathshapes
squareSize = 400
divs = 20
#start top, go clockwise
outerSquare = [Point(0, squareSize), Point(squareSize, 0), Point(0, -1*squareSize), Point(-1*squareSize,0)]
innerSquare = []
for i in range(0,4):
    innerSquare.append(getMidpoint(outerSquare[i], outerSquare[(i+1)%4]))

def makeSplay(docu, points, divs):
    ticks1 = getLineDivisions(points[0], points[1], divs)
    ticks2 = getLineDivisions(points[1], points[2], divs)
    splayGroup = docu.makeGroup()
    
    for i in range(divs):
        splayGroup.appendChild(buildLine(docu, ticks1[i], ticks2[i], {'style':'stroke:black; stroke-width:1'}))
    return splayGroup
    
def splayTriangle(docu, points, divs):
    splaydTriGroup = docu.makeGroup()
    for i in range(3):
        splaydTriGroup.appendChild(makeSplay(docu, [points[i], points[(i+1)%3], points[(i+2)%3] ], divs))
    return splaydTriGroup

docu = Document()
docu.appendElement(splayTriangle(docu, [innerSquare[0], outerSquare[0], innerSquare[3]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[1], outerSquare[1], innerSquare[0]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[2], outerSquare[2], innerSquare[1]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[3], outerSquare[3], innerSquare[2]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[0], Point(0,0), innerSquare[1]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[1], Point(0,0), innerSquare[2]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[2], Point(0,0), innerSquare[3]], divs  ) )
docu.appendElement(splayTriangle(docu, [innerSquare[3], Point(0,0), innerSquare[0]], divs  ) )

docu.writeSVG('sunburst.svg')
print "done"
