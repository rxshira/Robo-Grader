from PIL import Image
import os
import math


# Threshold for difference between pixel's color's component squared to the other two color's components squared.(think RMS)
# if the difference is above this threshold, it means that the pixel's color is actually that color component
colorSignificanceThreshold = 3000 # I found that this number works well
class Area:
     def __init__(self, left, right, top, bottom):
         self.left = left
         self.right = right
         self.top = top
         self.bottom = bottom
     def __repr__(self):
         return f"left:{self.left}, right:{self.right}, top:{self.top}, bottom:{self.bottom}"

     #check of other is overlapping
     def isOverlapping(self, other):
        # top left corner is in
        if self.left <= other.left <= self.right and self.top <= other.top <= self.bottom:
            return True
        # top right corner is in
        if self.left <= other.right <= self.right and self.top <= other.top <= self.bottom:
            return True
        # bottom left corner is in
        if self.left <= other.left <= self.right and self.top <= other.bottom <= self.bottom:
            return True
        # bottom right corner is in
        if self.left <= other.right <= self.right and self.top <= other.bottom <= self.bottom:
            return True
        return False

     def asPoint(self):
         robotEndPointX = self.left + (self.right - self.left) / 2
         robotEndPointY = self.top + (self.bottom - self.top) / 2
         return Point(robotEndPointX, robotEndPointY)

class TrackedArea:
    def __init__(self, area, imageIndex):
        self.area = area
        self.imageIndex = imageIndex

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def decreaseBy(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def increaseBy(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def distanceFromOrigin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angleAboveXAxis(self):
        return math.atan2(self.y, self.x)

    def scale(self, factor):
        self.x *= factor
        self.y *= factor

    def rotateAroundTheOrigin(self, rotationAngle): #https://en.wikipedia.org/wiki/Rotation_matrix
        rotatedX = self.x * math.cos(rotationAngle) - self.y * math.sin(rotationAngle)
        rotatedY = self.x * math.sin(rotationAngle) + self.y * math.cos(rotationAngle)
        self.x = rotatedX
        self.y = rotatedY

class Path:
    def __init__(self, start, end, points):
        self.start = start
        self.end = end
        self.points = points

    def __repr__(self):
        return f"{self.start} -> {self.end} ({len(self.points)})"



# the idea in these 3 functions - if a pixel has a significanly higher value for a specific color, than it is that color
# we sqaure the values of r,g,b and how far the color we check is from the sum of the two others
def isGreen(r,g,b):
    sqaureDiff = g ** 2 - b ** 2 - r ** 2
    return sqaureDiff > colorSignificanceThreshold

def isBlue(r,g,b):
    sqaureDiff = b ** 2 - g ** 2 - r ** 2
    return sqaureDiff > colorSignificanceThreshold

def isRed(r,g,b):
    sqaureDiff = r ** 2 - g ** 2 - b ** 2
    return sqaureDiff > colorSignificanceThreshold

def trackColor(folderPath, fileName, color):

    lastKnownTrackedArea = Area(0, 10000, 10000, 0)
    imageIndex = 0
    areaList = []
    maxChangeInPixels = 30 # max change in robot's position between each of the frames
    while os.path.isfile(f"{folderPath}\\{fileName}{imageIndex}.png"):
        im = Image.open(f"{folderPath}\\{fileName}{imageIndex}.png")
        imageIndex+=1
        rows, cols = im.size
        leftMost = topMost = 10000 #size that is bigger than any image
        rightMost = bottomMost = 0
        for i in range(rows):
            if i < lastKnownTrackedArea.left-maxChangeInPixels or i > lastKnownTrackedArea.right+maxChangeInPixels:
                continue
            for j in range(cols):
                if j > lastKnownTrackedArea.top+maxChangeInPixels or j < lastKnownTrackedArea.bottom-maxChangeInPixels:
                    continue
                r,g,b = im.getpixel((i, j))
                if (color == "blue" and isBlue(r, g, b)) or \
                        (color == "green" and isGreen(r,g,b)) or \
                        (color == "red" and isRed(r,g,b)):
                    if i < leftMost:
                        leftMost = i
                    if i > rightMost:
                        rightMost = i
                    if j < topMost:
                        topMost = j
                    if j > bottomMost:
                        bottomMost = j
        if leftMost == 10000: #didn't find any area
            continue
        lastKnownTrackedArea = Area(leftMost, rightMost, topMost, bottomMost)
        trackedArea = TrackedArea(lastKnownTrackedArea, imageIndex)
        areaList.append(trackedArea)
        # print(imageIndex) <-- uncomment this if you'd like to have the program list which frame it is going through
    return areaList

def asVectorFromOrigin(startPoint, endPoint):
    return endPoint.decreaseBy(startPoint)

# my approach to transforming/ rotation the path:
# think of the drawn start points and end point as one vector (aka drawnVector)
# and the robot's start point and end point as another vector (aka robotVector)
# 1) calculate what needs to be done in order to rotate and scale the drawnVector to become the
# robotVector.
# 2) use the same rotation and scaling to each point in the drawn path
# Used copilot to help me in creating this function
def transformPath(path, newStartPoint, newEndPoint):
    # change the points to vectors (i.e., move them to start from the origin)
    drawnVectorFromOrigin = asVectorFromOrigin(path.start, path.end)
    robotVectorFromOrigin = asVectorFromOrigin(newStartPoint, newEndPoint)

    # Calculate the lengths of the vectors
    lenDrawnVector = drawnVectorFromOrigin.distanceFromOrigin()
    lenRobotVector = robotVectorFromOrigin.distanceFromOrigin()

    scaleFactor = lenRobotVector / lenDrawnVector
    rotation = robotVectorFromOrigin.angleAboveXAxis() - drawnVectorFromOrigin.angleAboveXAxis()

    newPath = []
    # have each point as a vector from the start point to that point, and have it scaled and rotated
    for pt in path.points:
        pointAsVectorFromOrigin = asVectorFromOrigin(path.start, pt)
        pointAsVectorFromOrigin.scale(scaleFactor)
        pointAsVectorFromOrigin.rotateAroundTheOrigin(rotation)
        newPath.append(pointAsVectorFromOrigin.increaseBy(newStartPoint))
    return newPath

def squareToPoint(squareCoord, squareDim):
    x, y = squareCoord.coordx, squareCoord.coordy
    startPointX = x + squareDim / 2
    startPointY = y + squareDim / 2
    return Point(startPointX, startPointY)

def drawingToPath(startSquare, startSquareDim, endSquare, endSquareDim, path):
    startPoint = squareToPoint(startSquare, startSquareDim)
    endPoint = squareToPoint(endSquare, endSquareDim)
    pointsOnPath = []
    for p in path:
        pt = Point(p.coordx, p.coordy)
        pointsOnPath.append(pt)
    return Path(startPoint, endPoint, pointsOnPath)

def analyzeRobotPath(trackedAreaList, loadedImage, color):
    pathDictionary = dict()
    for trackedArea in trackedAreaList: #tracking and coloring with cyan
        area = trackedArea.area
        for i in range(area.left, area.right):
            for j in range(area.top, area.bottom):
                if j not in pathDictionary:
                    pathDictionary[j] = set()
                pathDictionary[j].add(i)
                loadedImage[i, j] = color
    return pathDictionary

def analyzeDrawnPath(drawnPath, robotPath, loadedImage):
    cntPointInRobotPath = 0
    markedDrawnPathWidth = 4
    markedDrawnPathHeight = 2
    pathMatchColor = (0,0, 0)
    pathNotMatchingColor = (255, 0, 0)
    for p in drawnPath:
        color = pathNotMatchingColor
        if int(p.y) in robotPath:
            if int(p.x) in robotPath[int(p.y)]:
                cntPointInRobotPath += 1
                color = pathMatchColor
        for i in range(markedDrawnPathWidth):
            for j in range(markedDrawnPathHeight):
                loadedImage[p.x+i, p.y+j] = color
                loadedImage[p.x - i, p.y - j] = color
    score = (cntPointInRobotPath * 1.0) / (len(drawnPath) * 1.0)
    return score

# !! important
def start(startSquare, startSquareDim, endSquare, endSquareDim, path, imagesLoction):
    folderPath = imagesLoction
    fileName = ""

    greenAreaList = trackColor(folderPath, fileName, "green")
    blueAreaList = trackColor(folderPath, fileName, "blue")

    im0 = Image.open(f"{folderPath}\\{fileName}0.png")
    loadedImage = im0.load()

    robotPath = analyzeRobotPath(blueAreaList, loadedImage, (0, 255, 255))

    drawnPath = drawingToPath(startSquare, startSquareDim, endSquare, endSquareDim, path)

    robotStartPoint = blueAreaList[0].area.asPoint()
    robotEndPoint = greenAreaList[0].area.asPoint()

    newPath = transformPath(drawnPath, robotStartPoint, robotEndPoint)
    score = analyzeDrawnPath(newPath, robotPath, loadedImage)
    if blueAreaList[-1].imageIndex > greenAreaList[-1].imageIndex:
        print("successful")
    if blueAreaList[-1].area.isOverlapping(greenAreaList[-1].area):
        print("very successful")
    print("success score= " + str(score))
    im0.show()

def percentAccuracy(startSquare, startSquareDim, endSquare, endSquareDim, path, imagesLoction): #newly added on attempt to single out percent
    folderPath = imagesLoction
    fileName = ""

    greenAreaList = trackColor(folderPath, fileName, "green")
    blueAreaList = trackColor(folderPath, fileName, "blue")

    im0 = Image.open(f"{folderPath}\\{fileName}0.png")
    loadedImage = im0.load()

    robotPath = analyzeRobotPath(blueAreaList, loadedImage, (0, 255, 255))

    drawnPath = drawingToPath(startSquare, startSquareDim, endSquare, endSquareDim, path)

    robotStartPoint = blueAreaList[0].area.asPoint()
    robotEndPoint = greenAreaList[0].area.asPoint()

    newPath = transformPath(drawnPath, robotStartPoint, robotEndPoint)
    score2 = analyzeDrawnPath(newPath, robotPath, loadedImage)

    return ((score2*1000000) // 1000) / 10.0, im0
