from cmu_graphics import *
from robotPath import percentAccuracy


class ExampleProjectScreen:
    def onAppStart(self, app):
        app.exampleProjTitle = (200, 40)

        app.selectVideoCoords = (50, 135)
        app.drawExButtonCoords = (50, 210)
        app.compareExButtonCoords = (50, 285)
        app.backButtonCoordsExample = (5, 345)
        app.helpButtonCoordsExample = (5, 370)

        app.buttonSizeExample = (300, 50)
        app.smallbuttonSizeExample = (40, 20)

        app.urlExample = 'https://i.pinimg.com/736x/bf/5b/8c/bf5b8c4c6aca20e208e9f36f5dfdb323.jpg'  # i made this
        app.urlUncheck = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWAyoLRmKqQ_b-ohRAo-VPD1iZKe156KKyBuRA3_3TQ9pSOnXGP1h-W2UhJx9VzmXhg4PwXc6Dvs2YICCVOYOjSSZn1X0NfLVX7xuGcwnSEt0e3HY40dwQaSiQnS-VEWXmzusNaW2NXXxZUyz2gFrIaUkO5emKj9Zcn4znELv8rEqyPqEeBAiaMeS9LU_e/s50/uncheck.png'
        app.urlCheck = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO9gXYNRkq_JrTHT8iNTKMG3H68sFfOscrAsXwhzf7HewnyPFPjII5XWb6Zp6q2aeMqm687pCqprM8u2kyxZoBnLxW5MIVivU6ijuAZgfnYz9MUJOYyGk2G8EjbF5sz3gYrbGJv7lobvxmjSAt4e0DcikAuNPixwyTAg9KG7z8TlcochklCgTsXDUKUKsY/s50/check.png'


        #this is for title of the video
        app.selectedExample = 'No Video Chosen'
        app.straightLineRobot = 'Straight Forward'
        app.zigZagRobot = 'Zig - Zag'
        app.mazeRobot = 'Maze Traversal'
        app.wobblyRobot = 'Wobbly - Bot'
        app.circleDanceRobot = 'Circle Dance'

        app.number = 22.46

        app.color1 = rgb(255, 0, 0)  # 0 - 10 red
        app.color2 = rgb(255, 131, 23)  # 10 - 30 orange
        app.color3 = rgb(245, 232, 56)  # 30 - 50 yellow
        app.color4 = rgb(163, 245, 56)  # 50 - 70 light green
        app.color5 = rgb(26, 245, 22)  # 70 - 90 neon green
        app.color6 = rgb(41, 187, 255)  # 90 - 99 blue
        app.color7 = rgb(77, 77, 255)  # 100 purple
        app.colorScore = 'black'
        self.colorOfScore(app)

    def isPressOnButton(self, buttonCoord, buttonSize, mouseX, mouseY): #Co-Pilot came up with this
        x, y = buttonCoord[0], buttonCoord[1]
        w, h = buttonSize[0], buttonSize[1]
        return x <= mouseX <= x + w and y <= mouseY <= y + h

    def onMousePress(self, app, mouseX, mouseY):
        if self.isPressOnButton(app.selectVideoCoords, app.buttonSizeExample, mouseX, mouseY):
            return 'Select Example Video'
        elif self.isPressOnButton(app.drawExButtonCoords, app.buttonSizeExample, mouseX, mouseY):
            return 'draw'
        elif self.isPressOnButton(app.compareExButtonCoords, app.buttonSizeExample, mouseX, mouseY):
            if app.uploadComplete and app.isDrawingComplete:
                app.number, app.image = percentAccuracy(app.newStartSquare, app.startSquareSize, app.newEndSquare,
                                                        app.endSquareSize, app.inks, app.framesLocation)
                self.colorOfScore(app)
                return 'compare'
            else:
                return 'example error'
        elif self.isPressOnButton(app.backButtonCoordsExample, app.smallbuttonSizeExample, mouseX, mouseY):
            return 'example back'
        elif self.isPressOnButton(app.helpButtonCoordsExample, app.smallbuttonSizeExample, mouseX, mouseY):
            return 'example help'
        return False

    def colorOfScore(self, app):
        if app.number < 10:
            app.colorScore = app.color1
        elif app.number < 30:
            app.colorScore = app.color2
        elif app.number < 50:
            app.colorScore = app.color3
        elif app.number < 70:
            app.colorScore = app.color4
        elif app.number < 90:
            app.colorScore = app.color5
        elif app.number < 100:
            app.colorScore = app.color6
        elif app.number == 100:
            app.colorScore = app.color7

    def drawButton(self, buttonCoords, buttonSize, text, labelSize, borderWidth, rectFillColor): #copilot's work
        x, y = buttonCoords[0], buttonCoords[1]
        w, h = buttonSize[0], buttonSize[1]
        drawRect(x, y, w, h, fill=rectFillColor, border='black', borderWidth=borderWidth)
        labelX = x + w / 2
        labelY = y + h / 2
        drawLabel(text, labelX, labelY, fill='black', bold=True, size=labelSize)

    def redrawAll(self, app):
        drawImage(app.urlExample, 0, 0)

        drawLabel('Example Projects', app.exampleProjTitle[0], app.exampleProjTitle[1], bold=True, fill='black',
                  font='monospace',
                  size=30)

        drawLabel(app.selectedExample, 200, 100, fill='black', bold= True, size=22)

        # Upload button
        self.drawButton(app.selectVideoCoords, app.buttonSizeExample, 'Select Project', 22, 5, 'white')
        # Draw button
        self.drawButton(app.drawExButtonCoords, app.buttonSizeExample, 'Draw Ideal Path', 22, 5, 'white')
        # Compare button
        self.drawButton(app.compareExButtonCoords, app.buttonSizeExample, 'Compare Paths', 22, 5, 'white')
        # Back button
        self.drawButton(app.backButtonCoordsExample, app.smallbuttonSizeExample, 'Back', 12, 3, 'LightGreen')
        # Help button
        self.drawButton(app.helpButtonCoordsExample, app.smallbuttonSizeExample, 'Help', 12, 3, 'LightGrey')
