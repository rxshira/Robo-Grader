from cmu_graphics import *
from types import SimpleNamespace
from robotPath import start

class UserFacing:
    def onAppStart(self, app):
        # Drawing related variables
        app.inks = []
        app.inkSize = 6
        app.drawCircleCenter = (375, 170)

        # Erasing related variables
        app.isEraserMode = False
        app.eraserCircleCenter = (375, 240)

        # Circles for drawing + erasing on the side
        app.circleRadius = 15

        # Canvas related variables
        app.canvasTopX = 50
        app.canvasTopY = 60
        app.canvasSize = 300

        # Dragging and moving start square related variables
        app.draggingStartSquare = False
        app.fixedStartSquare = False
        app.fixButtonCoords = (5, 185)
        app.fixButtonSize = (40, 20)

        # Start square related variables
        app.startSquareTopCoords = (10, 125)
        app.startSquareSize = 30
        app.newStartSquare = None

        # End square related variables
        app.endSquareTopCoords = (10, 225)
        app.endSquareSize = 30
        app.newEndSquare = None
        app.draggingEndSquare = False
        app.fixedEndSquare = False
        app.fixEndButtonCoords = (5, 285)

        # Smaller buttons
        app.backButtonCoordsDraw = (5, 345)
        app.helpButtonCoordsDraw = (5, 370)

        app.smallButtonSizeDraw = (40, 20)
        app.isDrawingComplete = False

    def isInkInsideSquare(self, ink, squareX, squareY, squareSize):
        x, y = ink.coordx, ink.coordy
        return squareX <= x <= squareX + squareSize and squareY <= y <= squareY + squareSize

    def makeInk(self, coordx, coordy):
        ink = SimpleNamespace()
        ink.size = 6
        ink.coordx = coordx
        ink.coordy = coordy
        ink.color = 'black'
        return ink

    def drawInk(self, app):
        for ink in app.inks:
            drawCircle(ink.coordx, ink.coordy, ink.size, fill=ink.color)

    def onKeyPress(self, app, key):
        if key == 'a':
            print(app.inks)
        if key == 'g':
            start(app.newStartSquare, app.startSquareSize, app.newEndSquare, app.endSquareSize, app.inks,
                  app.framesLocation)

    def insideDrawingArea(self, app, mouseX, mouseY):
        return (
                mouseX > (app.canvasTopX + (app.startSquareSize / 2)) and
                mouseX < (app.canvasTopX + app.canvasSize - (app.startSquareSize / 2)) and
                mouseY > (app.canvasTopY + (app.startSquareSize / 2)) and
                mouseY < (app.canvasTopY + app.canvasSize - (app.startSquareSize / 2))
        )

    def insideEndSquare(self, app, mouseX, mouseY, coords):
        x, y = coords
        return (x <= mouseX <= x + app.endSquareSize) and (y <= mouseY <= y + app.endSquareSize)

    def insideFixButton(self, app, mouseX, mouseY, buttonCoords, buttonSize):
        x, y = buttonCoords
        w, h = buttonSize
        return (x <= mouseX <= x + w) and (y <= mouseY <= y + h)

    def insideCircle(self, cx, cy, radius, mouseX, mouseY):
        return self.distance(cx, cy, mouseX, mouseY) <= radius

    def checkConnectionAndEraseIfNeeded(self, app): #some support from Microsoft Copilot here
        if not app.newStartSquare or not app.newEndSquare:
            return  False # No start or end square to check against

        # Define boundaries of the red and green squares
        startX1, startY1 = app.newStartSquare.coordx, app.newStartSquare.coordy
        startX2, startY2 = startX1 + app.newStartSquare.size, startY1 + app.newStartSquare.size

        endX1, endY1 = app.newEndSquare.coordx, app.newEndSquare.coordy
        endX2, endY2 = endX1 + app.newEndSquare.size, endY1 + app.newEndSquare.size

        # Check if any ink point is inside the red square (from copilot)
        connectsStart = any(startX1 <= ink.coordx <= startX2 and startY1 <= ink.coordy <= startY2 for ink in app.inks)

        # Check if any ink point is inside the green square (from copilot)
        connectsEnd = any(endX1 <= ink.coordx <= endX2 and endY1 <= ink.coordy <= endY2 for ink in app.inks)

        # If not connected to both squares, clear the ink
        if not (connectsStart and connectsEnd):
            app.inks = []
            return False
        return True

    def isLineValid(self, app): #lots of help in this method from microsoft co-pilot
        if len(app.inks) < 2:
            return False  # not enough points to form a line

        # Handle start square coordinates
        if app.newStartSquare:
            startX, startY, size = app.newStartSquare.coordx, app.newStartSquare.coordy, app.newStartSquare.size
        else:
            startX, startY, size = app.startSquareTopCoords[0], app.startSquareTopCoords[1], app.startSquareSize

        # Handle end square coordinates
        if app.newEndSquare:
            endX, endY, endSize = app.newEndSquare.coordx, app.newEndSquare.coordy, app.newEndSquare.size
        else:
            endX, endY, endSize = app.endSquareTopCoords[0], app.endSquareTopCoords[1], app.endSquareSize

        # Check if at least one point is inside the start square and one point inside the end square
        startConnected = any(self.isInkInsideSquare(ink, startX, startY, size) for ink in app.inks)
        endConnected = any(self.isInkInsideSquare(ink, endX, endY, endSize) for ink in app.inks)

        # Return False if either square doesn't exist
        if not startConnected or not endConnected:
            return False

        return startConnected and endConnected

    def onMouseRelease(self, app, mouseX, mouseY):
        if not self.isLineValid(app):
            app.inks.clear()  # Clear all drawn points if the line is invalid
            app.isDrawingComplete = False
        else:
            app.isDrawingComplete = True

    def onMouseDrag(self, app, mouseX, mouseY):
        if not app.newStartSquare or not app.newEndSquare:
            return
        if app.draggingStartSquare and not app.fixedStartSquare and self.insideDrawingArea(app, mouseX, mouseY):
            app.newStartSquare.coordx = mouseX - app.newStartSquare.size / 2
            app.newStartSquare.coordy = mouseY - app.newStartSquare.size / 2

        elif app.draggingEndSquare and not app.fixedEndSquare and self.insideDrawingArea(app, mouseX, mouseY):
            app.newEndSquare.coordx = mouseX - app.newEndSquare.size / 2
            app.newEndSquare.coordy = mouseY - app.newEndSquare.size / 2

        elif not app.draggingStartSquare and not app.draggingEndSquare and self.insideDrawingArea(app, mouseX, mouseY):
            ink = self.makeInk(mouseX, mouseY)
            app.inks.append(ink)


    def onMousePress(self, app, mouseX, mouseY):
        if self.insideCircle(app.eraserCircleCenter[0], app.eraserCircleCenter[1], app.circleRadius, mouseX, mouseY):
            app.inks.clear()
        elif self.insideStartSquare(app, mouseX, mouseY, app.startSquareTopCoords):
            if not app.newStartSquare:
                app.newStartSquare = SimpleNamespace(
                    coordx=app.canvasTopX + app.canvasSize - app.startSquareSize - app.inkSize,
                    coordy=app.canvasTopY + app.canvasSize - app.startSquareSize - app.inkSize,
                    size=app.startSquareSize)
        elif self.insideEndSquare(app, mouseX, mouseY, app.endSquareTopCoords):
            if not app.newEndSquare:
                app.newEndSquare = SimpleNamespace(
                    coordx=app.canvasTopX + app.inkSize,
                    coordy=app.canvasTopY + app.canvasSize - app.endSquareSize - app.inkSize,
                    size=app.endSquareSize)
        elif self.insideFixButton(app, mouseX, mouseY, app.fixButtonCoords, app.fixButtonSize):
            app.fixedStartSquare = not app.fixedStartSquare
        elif self.insideFixButton(app, mouseX, mouseY, app.fixEndButtonCoords, app.fixButtonSize):
            app.fixedEndSquare = not app.fixedEndSquare

        elif app.newStartSquare and self.insideDrawingArea(app, mouseX, mouseY) and self.insideStartSquare(app, mouseX, mouseY, (
                app.newStartSquare.coordx, app.newStartSquare.coordy)):
            if not app.fixedStartSquare:
                app.draggingStartSquare = not app.draggingStartSquare


        elif app.newEndSquare and self.insideDrawingArea(app, mouseX, mouseY) and self.insideEndSquare(app, mouseX, mouseY, (
                app.newEndSquare.coordx, app.newEndSquare.coordy)):
            if not app.fixedEndSquare:
                app.draggingEndSquare = not app.draggingEndSquare

        elif (app.backButtonCoordsDraw[0] <= mouseX <= app.backButtonCoordsDraw[0] + app.smallButtonSizeDraw[0] and
                app.backButtonCoordsDraw[1] <= mouseY <= app.backButtonCoordsDraw[1] + app.smallButtonSizeDraw[1]):
            return 'draw back'

        elif (app.helpButtonCoordsDraw[0] <= mouseX <= app.helpButtonCoordsDraw[0] + app.smallButtonSizeDraw[0] and
              app.helpButtonCoordsDraw[1] <= mouseY <= app.helpButtonCoordsDraw[1] + app.smallButtonSizeDraw[1]):
            return 'draw help'


    def onMouseRelease(self, app, mouseX, mouseY): #gpt
        app.isDrawingComplete = self.checkConnectionAndEraseIfNeeded(app)
        app.draggingStartSquare = False
        app.draggingEndSquare = False


    def insideStartSquare(self, app, mouseX, mouseY, coords):
        x, y = coords
        return (x <= mouseX <= x + app.startSquareSize) and (y <= mouseY <= y + app.startSquareSize)

    def distance(self, x0, y0, x1, y1):
        return (((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5

    def drawCircleButton(self, position, radius, fill, border, text): #Co-Pilot's idea
        drawCircle(position[0], position[1], radius, fill=fill, border=border)
        drawLabel(text, position[0], position[1] + 30, size=12)

    def drawRectButton(self, position, fill, text, isBold, textSize, labelY, width, height=0): #Co-Pilot's idea
        height = height if height > 0 else width
        drawRect(position[0], position[1], width, height, fill=fill, border='black')
        drawLabel(text, position[0] + width/2, labelY, size=textSize, bold=isBold)


    def redrawAll(self, app):
        #text
        drawLabel('Draw your ideal path for the robot!', 200, 35, bold=True, size=16, font='monospace')

        drawRect(app.canvasTopX, app.canvasTopY, app.canvasSize, app.canvasSize, border='black', fill=None)
        self.drawInk(app)

        self.drawCircleButton(app.eraserCircleCenter, app.circleRadius, 'pink', 'black', 'Clear')
        self.drawCircleButton(app.drawCircleCenter, app.circleRadius, 'black', 'red', 'Draw')

        # Start square drawing
        self.drawRectButton(app.startSquareTopCoords, 'crimson', 'Start', False, 12,
                            app.startSquareTopCoords[1] + app.startSquareSize + 17, app.startSquareSize)
        if app.newStartSquare:
            drawRect(app.newStartSquare.coordx, app.newStartSquare.coordy, app.newStartSquare.size,
                     app.newStartSquare.size, fill='crimson', border='black')

        # Draw the fix button
        buttonLabel = "Fix" if not app.fixedStartSquare else "Unfix"
        self.drawRectButton(app.fixButtonCoords,'gray', buttonLabel, False, 10,
                            app.fixButtonCoords[1] + app.fixButtonSize[1] / 2, app.fixButtonSize[0], app.fixButtonSize[1])

        # End square drawing
        self.drawRectButton(app.endSquareTopCoords, 'green', 'End', False, 12,
                            app.endSquareTopCoords[1] + app.endSquareSize + 17, app.endSquareSize)
        if app.newEndSquare:
            drawRect(app.newEndSquare.coordx, app.newEndSquare.coordy, app.newEndSquare.size, app.newEndSquare.size,
                     fill='green', border='black')

        # Draw the fix button for the end square
        buttonLabelEnd = "Fix" if not app.fixedEndSquare else "Unfix"
        self.drawRectButton(app.fixEndButtonCoords, 'gray', buttonLabelEnd, False, 10,
                            app.fixEndButtonCoords[1] + app.fixButtonSize[1] / 2, app.fixButtonSize[0], app.fixButtonSize[1])

        # back button
        backButtonDrawLabelY = app.backButtonCoordsDraw[1] + app.smallButtonSizeDraw[1] / 2
        self.drawRectButton(app.backButtonCoordsDraw, 'lightGreen', 'Back', True, 12,
                            backButtonDrawLabelY, app.smallButtonSizeDraw[0], app.smallButtonSizeDraw[1])

        # help button
        helpButtonDrawLabelY = app.helpButtonCoordsDraw[1] + app.smallButtonSizeDraw[1] / 2
        self.drawRectButton(app.helpButtonCoordsDraw,'lightGrey', 'Help', True, 12,
                            helpButtonDrawLabelY, app.smallButtonSizeDraw[0], app.smallButtonSizeDraw[1])
