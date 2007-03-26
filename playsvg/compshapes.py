
'''This module builds composite shapes and returns amara xml nodes containing them'''

#FIXME: separate methods that return only a node containing a single path and make them return only the PathData object itself  

from playsvg.geom import *
from playsvg.element import *
import playsvg.pathshapes

#CODE not compatible with new Document to replace Base
###FIXME: create method for creating true vesica pisces shapes
##
##def buildSubunitWheel(base, pssSpoke, pssLayer, axleRadius, wheelRadius, attrList=()):
##    '''Builds a wheel with spokes of varying widths to represent subunit division i.e. ruler ticks.  
##    pss is represented as a list of (division, width) pairs (division being > 1).  The first division divides the wheel 
##    into any number of sections.  Every subsequent division divides all sections into the 
##    specified number of subsections.'''
##    wheelGroup = base.dok.xml_element(u'g')
##    wheelGroup.xml_append(buildCircle(base,Point(0,0), axleRadius,attributes={u'fill':u'none', u'stroke-width':u'13', u'stroke':u'black', u'stroke-opacity':u'1'}))
##    wheelGroup.xml_append(buildCircle(base,Point(0,0), wheelRadius, attributes={u'fill':u'none', u'stroke-width':u'13', u'stroke':u'black', u'stroke-opacity':u'1'}))
##    
##    #Spoke subdivision
##    dividedInto=1
##    print len(pssSpoke)
##    for i in range(0,len(pssSpoke)):
##        print "ieeee" + str(i)
##        if i != 0: 
##            divdedInto = dividedInto*pssSpoke[i-1][0]
##        toDivideInto = dividedInto*pssSpoke[i][0]
##        print "dividedinto"+str(dividedInto)
##        print "todividedinto:" + str(toDivideInto)
##        for j in range(0, toDivideInto):
##            if j % (toDivideInto/dividedInto)  != 0 or i==0 :  #if there is no division made at j or we're in the first round of divisions make one
##                print j
##                wheelGroup.xml_append( \
##                buildLine(base, \
##                    PolerPoint(axleRadius, float(j)/toDivideInto).convertToCartesian(), \
##                    PolerPoint(wheelRadius, float(j)/toDivideInto).convertToCartesian(), \
##                    attributes={u'stroke-width':unicode(pssSpoke[i][1])})) 
##        dividedInto=toDivideInto
##    
##    # Layer subdivision
##    dividedInto=1
##    totalRadius = wheelRadius - axleRadius
##    for i in range(0,len(pssLayer)):
##        print "ieeee" + str(i)
##        if i != 0: 
##            divdedInto = dividedInto*pssLayer[i-1][0]
##        toDivideInto = dividedInto*pssLayer[i][0]
##        print "dividedinto"+str(dividedInto)
##        print "todividedinto:" + str(toDivideInto)
##        for j in range(0, toDivideInto):
##            if j % (toDivideInto/dividedInto)  != 0 or i==0 :  #if there is no division made at j or we're in the first round of divisions make one
##                print j
##                wheelGroup.xml_append( \
##                buildCircle(base, \
##                    Point(0,0), \
##                    (axleRadius + totalRadius*(float(j)/toDivideInto)) , \
##                    attributes={u'fill':u'none',u'stroke-width':unicode(pssLayer[i][1])})) 
##        dividedInto=toDivideInto
##                
##    
##    return wheelGroup 
##    
##def buildSubunitTicks(base, pss, startX, endX,  height):
##    '''Builds a wheel with spokes of varying widths to represent subunit division i.e. ruler ticks.  
##    pss is represented as a list of (division, width) pairs (division being > 1).  The first division divides the wheel 
##    into any number of sections.  Every subsequent division divides all sections into the 
##    specified number of subsections.'''
##    tickGroup = base.dok.xml_element(u'g')
##    start = Point(startX,0)
##    end = Point(endX, 0)
##    dividedInto=1
##    print len(pss)
##    for i in range(0,len(pss)):
##        print "ieeee" + str(i)
##        if i != 0: 
##            divdedInto = dividedInto*pss[i-1][0]
##        toDivideInto = dividedInto*pss[i][0]
##        print "dividedinto"+str(dividedInto)
##        print "todividedinto:" + str(toDivideInto)
##        for j in range(0, toDivideInto):
##            if j % (toDivideInto/dividedInto)  != 0 or i==0 :  #if there is no division made at j or we're in the first round of divisions make one
##                print j
##                basePoint = getLineDivision(start, end, float(j)/toDivideInto)
##                tickGroup.xml_append(buildLine(base, basePoint,  Point(basePoint.x, pss[i][1]*height) ) )
##        dividedInto=toDivideInto
##    tickGroup.xml_append(buildLine(base, Point(endX,0),  Point(endX, pss[0][1]*height) ) )
##    return tickGroup
##
##    
##def buildPolyRadial(base, sides, shapeRadius, spokeRadius, ctrlLengthRatio, ctrlAngle, numSpokes):
##    polyTips = []
##    controlPoints = []
##    spokeRadi = []
##    for i in range(sides):
##        polyTips.append(PolerPoint(shapeRadius, float(i)/sides).convertToCartesian())
##        spokeRadi.append(PolerPoint(spokeRadius, (i+0.5)/sides).convertToCartesian())
##            
##    sideDistance = distanceBetween(polyTips[0], polyTips[1])
##    pathData = PathData().moveTo(polyTips[0])
##        
##    for i in range(sides):
##        startPoint = polyTips[i]
##        endPoint = polyTips[(i+1) % sides]
##        ctrlPt1 = hingePlot(startPoint, endPoint, ctrlLengthRatio*sideDistance, ctrlAngle)
##        ctrlPt2 = hingePlot(endPoint, startPoint, ctrlLengthRatio*sideDistance, -1*ctrlAngle)
##        pathData.cubicBezier(ctrlPt1, ctrlPt2, endPoint)
##        sideTicks = getDiscreteCubicBezier(startPoint, ctrlPt1, ctrlPt2, endPoint, numSpokes)
##        for j in range(len(sideTicks)):
##            spireGroup.xml_append(buildLine(base, sideTicks[j], spokeRadi[i]))
##    
##    spireGroup.xml_append(buildPath(base, pathData))
##    return spireGroup
##    
##def buildCircleCartoid(base, circles, radius):
##    '''Creates a series of circles whose envelope forms a cartoid.\
##    Inspired by http://mathworld.wolfram.com/Cardioid.html.  Motivated by  \
##    the possibility of a Valentine's Day T-Shirt that says "eat my cartoid out'''
##    
##    cartOutlineGroup = base.dok.xml_element(u'g')
##    cartFillGroup = base.dok.xml_element(u'g')
##    cartGroup = base.dok.xml_element(u'g')
##    
##    centrePoint = Point(0,0)
##    focusPoint = PolerPoint(radius,0).convertToCartesian()
##    
##    for i in range(circles):
##        currentPoint = PolerPoint(radius, float(i)/circles).convertToCartesian()
##        distance = distanceBetween(focusPoint, currentPoint)
##        cartOutlineGroup.xml_append(buildCircle(base, currentPoint, distance, attributes = {u'fill':u'none',u'style':u'opacity:1.0000000;fill:none;fill-opacity:0.35714284;fill-rule:evenodd;stroke:#ffffff;stroke-width:3;stroke-linejoin:round;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-dashoffset:0.0000000;stroke-opacity:1.0000000'}))
##        #cartFillGroup.xml_append(buildCircle(base, currentPoint, distance, attributes = {u'style':u'opacity:0.4000000;fill:#ff0041;fill-opacity:0.35714284;fill-rule:evenodd;stroke:none;stroke-width:11.700000;stroke-linejoin:round;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-dashoffset:0.0000000;stroke-opacity:1.0000000'}))
##
##    #cartGroup.xml_append(cartFillGroup)
##    cartGroup.xml_append(cartOutlineGroup)
##    
##    return cartGroup
##    
##
##    
##
##def buildStringArt(base, divs, size):
##    stringArtGroup = base.dok.xml_element(u'g')
##    corners = []
##    corners.append(Point(size,size))
##    corners.append(Point(size, -1*size))
##    corners.append(Point(-1*size, -1*size))
##    corners.append(Point(-1*size, size))
##    points = []
##    
##    for i in range(0,4):
##        points = []
##        points.append(getLineDivisions(corners[i], corners[(i+1)%4],divs) )
##        points.append(getLineDivisions(corners[(i+1)%4], corners[(i+2)%4], divs))
##        
##        for j in range(0, int(math.floor(divs/2.0))):
##            stringArtGroup.xml_append(buildLine(base,points[0][j+int(math.ceil(divs/2.0))], points[1][j+1]))
##    
##    return stringArtGroup
##
##def buildTrianglePath(point, radius):
##    triangleCorners = []
##    trianglePath = PathData()
##    for i in range(0,3):
##        triangleCorners.append(PolerPoint(radius, float(i)/3).convertToCartesian() + point)
##    trianglePath.moveTo(triangleCorners[0])
##    trianglePath.lineTo(triangleCorners[1])
##    trianglePath.lineTo(triangleCorners[2])
##    trianglePath.closePath()
##    return trianglePath
##  
##    
##def buildCubicBezierLengthTest(base,P1,P2,P3,P4):
##    '''places a bezier only of length estimated by approximation (using stroke-dashoffset atribute) on top of the full bezier to test the accuracy of estimation'''
##    length = cubicBezierLength(P1,P2,P3,P4)
##    print length
##    theNode = base.dok.xml_element(u'g')
##    realPath = PathData()
##    realPath.moveTo(P1)
##    realPath.cubicBezier(P2,P3,P4)
##    clipPath = buildPath(base, realPath, attributes={u'stroke-dasharray':unicode(length),u'stroke-dashoffset': unicode(length), u'stroke':u'red',u'stroke-opacity':u'0.5'} )
##    fullPath = buildPath(base, realPath, attributes={ u'stroke':u'black', u'stroke-opacity':u'0.5'} )
##    theNode.xml_append(clipPath)
##    theNode.xml_append(fullPath)
##    return theNode
##    ##def buildCircleSpiral(base, beginRadius, endRadius, beginCircleSize, endCircleSize    
##
##def aPathY(base):
##    pathData = PathData().moveTo(Point(0,0)).lineTo(Point(34,34)).lineTo(Point(90, -80)).lineTo(Point(23, 200)).lineTo(Point(500,500))
##    return buildPath(base, pathData)
##
###FIXME: I can't read in a file
####def addCirclesToNodes(base):
####    print base.dok.xml_doc()
####    pathData = PathData()
####    pathNode = base.searchByID('path1')
####    print pathNode
####    
##
##    
##def hexagonLatticeRadial(abase, level, radius):
##    
##    #define color ring array
##    colorGradation = color.tupleGradient((195,255,11), (195,155,247),level+1 )
##    print colorGradation
##    containerGroup = abase.dok.xml_element(u'g')
##    latticeGroup = abase.dok.xml_element(u'g')
##    latticeOutlineGroup = abase.dok.xml_element(u'g')
##    
##    
##    #add centre hexagon
##    latticeGroup.xml_append(buildPath(abase,pathshapes.hexagon( Point(0,0),radius), attributes = {u'style':u'fill-opacity:1;fill:'+unicode(colorGradation[0])}))
##    
##    distFromHex = radius*math.sin((0.5-1.0/6)*2*math.pi)/math.sin(1.0/12*2*math.pi)
##    
##    #creates a set of concentric hexagons
##    for i in range(1,level):
##        latticeRingGroup = abase.dok.xml_element(u'g') 
##        
##        #corners of an invisible hexagon on which the concentric hexagons will be centred on
##        hexagonFrame = []
##        
##        for j in range(6):
##            
##            hexagonFrame.append(PolerPoint(i*distFromHex , float(j)/6+1.0/12).convertToCartesian()) 
##            #FIXME: do trig to figure out the perfect ratio for the angle in the PolerPoint     
##        
##        #each line of the invisible hexagon is equally divided into n points where n is the layer number
##        #hexagons are plotted on these points
##        for j in range(6):
##            latticePath = PathData()
##            sidePoints = []
##            sidePoints.extend(getLineDivisions(hexagonFrame[j], hexagonFrame[(j+1)%6], i+1))
##            for k in range(len(sidePoints)):
##                latticeRingGroup.xml_append(buildPath(abase,pathshapes.hexagon(sidePoints[k], radius), attributes = {u'style': 'fill-opacity:1;fill:'+unicode(colorGradation[i])}))
##        latticeGroup.xml_append(latticeRingGroup)   
##        
##        
##    return latticeGroup
##
##def flowerOfLife(abase, centre, level, radius, circleAttributes ):
##    latticeRingOutlineGroup = abase.dok.xml_element(u'g')
##    
##    #add centre hexagon
##    
##    latticeRingOutlineGroup.xml_append(buildCircle(abase,centre, radius, attributes = circleAttributes))
##    distFromHex = radius*math.sin((0.5-1.0/6)*2*math.pi)/math.sin(1.0/12*2*math.pi)
##    
##    #creates a set of concentric hexagons
##    for i in range(1,level):
##        
##        
##        #corners of an invisible hexagon on which the concentric hexagons will be centred on
##        hexagonFrame = []
##        
##        for j in range(6):
##            hexagonFrame.append(PolerPoint(i*radius , float(j)/6+1.0/12).convertToCartesian()+centre) 
##            
##        #each line of the invisible hexagon is equally divided into n points where n is the layer number
##        #hexagons are plotted on these points
##        for j in range(6):
##            latticePath = PathData()
##            sidePoints = []
##            sidePoints.extend(getLineDivisions(hexagonFrame[j], hexagonFrame[(j+1)%6], i+1))
##            for k in range(len(sidePoints)-1):
##                if circleAttributes == {}:
##                    latticeRingOutlineGroup.xml_append(buildCircle(abase,sidePoints[k], radius, attributes = {u'style': u'stroke-width:1;stroke:black'}))
##                else:
##                    latticeRingOutlineGroup.xml_append(buildCircle(abase,sidePoints[k], radius, attributes = circleAttributes))
##    return latticeRingOutlineGroup
    

def buildHexagonLattice(docu,level, radius):
    latticePath = PathData()
    #add centre hexagon
    latticePath.appendPath(hexagon( Point(0,0),radius))
    distFromHex = radius*math.sin((0.5-1.0/6)*2*math.pi)/math.sin(1.0/12*2*math.pi)
    latticeGroup = docu.makeGroup('hexagonlattice')
    #creates a set of concentric hexagons
    for i in range(1,level):
        #corners of an invisible hexagon on which the concentric hexagons will be centred on
        hexagonFrame = []
        levelGroup = docu.makeGroup('level'+str(i))
        for j in range(6):
            
            hexagonFrame.append(PolerPoint(i*distFromHex , float(j)/6+1.0/12).convertToCartesian()) 
            #FIXME: do trig to figure out the perfect ratio for the angle in the PolerPoint     
        
        #each line of the invisible hexagon is equally divided into n points where n is the layer number
        #hexagons are plotted on these points
        for j in range(6):
            sidePoints = []
            sidePoints.extend(getLineDivisions(hexagonFrame[j], hexagonFrame[(j+1)%6], i+1))
            for k in range(len(sidePoints)):
                levelGroup.appendChild(buildPath(docu, playsvg.pathshapes.hexagon(sidePoints[k], radius),{'style':'stroke:black;fill:none'}  ))
        latticeGroup.appendChild(levelGroup)
        
    return latticeGroup

    
    
