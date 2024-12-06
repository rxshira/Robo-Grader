from cmu_graphics import *
from easygui import *
from vidToImg import extractFrames
from robotPath import percentAccuracy

class NewProjectScreen:
    def onAppStart(self, app):
        app.newProjTitle = (200, 40)

        app.uploadFileCoords = (50, 135)
        app.drawButtonCoords = (50, 210)
        app.compareButtonCoords = (50, 285)
        app.backButtonCoordsNew = (5, 345)
        app.helpButtonCoordsNew = (5, 370)

        app.buttonSize = (300, 50)
        app.smallButtonSize = (40, 20)

        app.url1 = 'https://i.pinimg.com/736x/a7/49/df/a749dfac215c3e1d91b82bf8ff5961dc.jpg'  # i made this
        app.urlUncheck = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWAyoLRmKqQ_b-ohRAo-VPD1iZKe156KKyBuRA3_3TQ9pSOnXGP1h-W2UhJx9VzmXhg4PwXc6Dvs2YICCVOYOjSSZn1X0NfLVX7xuGcwnSEt0e3HY40dwQaSiQnS-VEWXmzusNaW2NXXxZUyz2gFrIaUkO5emKj9Zcn4znELv8rEqyPqEeBAiaMeS9LU_e/s50/uncheck.png'
        app.urlCheck = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO9gXYNRkq_JrTHT8iNTKMG3H68sFfOscrAsXwhzf7HewnyPFPjII5XWb6Zp6q2aeMqm687pCqprM8u2kyxZoBnLxW5MIVivU6ijuAZgfnYz9MUJOYyGk2G8EjbF5sz3gYrbGJv7lobvxmjSAt4e0DcikAuNPixwyTAg9KG7z8TlcochklCgTsXDUKUKsY/s50/check.png'

        app.uploadCheckCoords = (300, 135)

        app.userTypedTitle = ''
        app.isTitleEditable = True
        app.isLabelBold = False

        app.uploadComplete = False

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

    def onKeyPress(self, app, key):
        if app.isTitleEditable:
            if key == 'backspace' and len(app.userTypedTitle) > 0:
                app.userTypedTitle = app.userTypedTitle[:-1]
            elif key == 'space' and len(app.userTypedTitle) > 0:
                app.userTypedTitle += ' '
            elif key == 'enter' and len(app.userTypedTitle) > 0:
                app.userTypedTitle = app.userTypedTitle
            elif len(app.userTypedTitle) < 14 and (key.isdigit() or key.isalpha()):
                app.userTypedTitle += key

    def isPressOnButton(self, buttonCoord, buttonSize, mouseX, mouseY):
        x,y = buttonCoord[0], buttonCoord[1]
        w,h = buttonSize[0], buttonSize[1]
        return x <= mouseX <= x+w and y <= mouseY <= y+h

    def onMousePress(self, app, mouseX, mouseY):
        # Check if the "Project Title:" label is clicked
        if (50 <= mouseX <= 350 and 85 <= mouseY <= 115):
            app.isLabelBold = not app.isLabelBold
            app.isTitleEditable = app.isLabelBold

        elif self.isPressOnButton(app.uploadFileCoords, app.buttonSize, mouseX, mouseY):
            self.uploadVideo()
        elif self.isPressOnButton(app.drawButtonCoords, app.buttonSize, mouseX, mouseY):
            return 'draw'
        elif self.isPressOnButton(app.compareButtonCoords, app.buttonSize, mouseX, mouseY):
            if app.uploadComplete and app.isDrawingComplete:
                app.number, app.image = percentAccuracy(app.newStartSquare, app.startSquareSize, app.newEndSquare,
                                                        app.endSquareSize, app.inks, app.framesLocation)
                self.colorOfScore(app)
                return 'compare'
            else:
                return 'new proj error'
        elif self.isPressOnButton(app.backButtonCoordsNew, app.smallButtonSize, mouseX, mouseY):
            return 'new back'
        elif self.isPressOnButton(app.helpButtonCoordsNew, app.smallButtonSize, mouseX, mouseY):
            return 'new help'
        return False

    def uploadVideo(self):
        videoFile = fileopenbox(title="Select a Robot video file", filetypes=[["*.mp4", "Video files"]])
        framesLocation = diropenbox(title="Select a folder to store frames")
        app.videoFile = videoFile
        app.framesLocation = framesLocation
        if app.videoFile is not None and app.framesLocation is not None:
            app.uploadComplete = True
            extractFrames(app.videoFile, app.framesLocation)
        else:
            app.uploadComplete = False

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


    def drawButton(self, buttonCoords, buttonSize, text, labelSize, borderWidth, rectFillColor): #microsoft copilot's suggestion for cleaner code
        x, y = buttonCoords[0], buttonCoords[1]
        w, h = buttonSize[0], buttonSize[1]
        drawRect(x,y,w,h, fill=rectFillColor, border='black', borderWidth=borderWidth)
        labelX = x + w / 2
        labelY = y + h / 2
        drawLabel(text, labelX, labelY, fill='black', bold=True, size=labelSize)

    def redrawAll(self,app):
        drawImage(app.url1, 0, 0)

        drawLabel('New Project', app.newProjTitle[0], app.newProjTitle[1], bold=True, fill='green', font='monospace',
                  size=30)

        drawLabel('Project Title:', 50, 100, fill='black', bold=app.isLabelBold, size=22, align='left')
        drawLine(180, 110, 350, 110)

        drawLabel(app.userTypedTitle, 180, 100, fill='black', size=22, align='left')


        # to make these drawings, i asked Co-pilot to help me write this cleaner, using the draw button function it made earlier. this is why it may look different from my other programs,
        # in this project where the style of drawing a button is different and less efficient.
        # i'd like to make this clear. THIS IS NOT WRITTEN BY ME! The idea is my own, but i asked for CoPilot to make it better.
        # Upload button
        self.drawButton(app.uploadFileCoords, app.buttonSize, 'Upload File', 22, 5, 'white')
        # Draw button
        self.drawButton(app.drawButtonCoords, app.buttonSize, 'Draw Ideal Path', 22, 5, 'white')
        # Compare button
        self.drawButton(app.compareButtonCoords, app.buttonSize, 'Compare Paths', 22, 5, 'white')
        # Back button
        self.drawButton(app.backButtonCoordsNew, app.smallButtonSize, 'Back', 12, 3, 'LightGreen')
        # Help button
        self.drawButton(app.helpButtonCoordsNew, app.smallButtonSize, 'Help', 12, 3, 'LightGrey')

        # Check Mark for Uploading,
        uploadStatusImage = app.urlCheck if app.uploadComplete else app.urlUncheck
        drawImage(uploadStatusImage, app.uploadCheckCoords[0], app.uploadCheckCoords[1])
        drawRect(app.uploadFileCoords[0], app.uploadFileCoords[1], app.buttonSize[0], app.buttonSize[1], fill=None,
                 border='black', borderWidth=5)