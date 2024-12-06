from cmu_graphics import *
from easygui import *
from vidToImg import *

class SelectExampleVideo:
    def onAppStart(self, app):
        app.selectVideoScreenTitle = (200, 50)

        app.straightForwardButtonCoords = (50, 90)
        app.wobblyBotButtonCoords = (50, 150)
        app.zigZagButtonCoords = (50, 210)
        app.circleDanceButtonCoords = (50, 270)
        app.mazeTraversalButtonCoords = (50, 330)
        app.selectVideoBackButtonCoords = (5, 370)

        app.selectVideoButtonSize = (300, 50)
        app.smallSelectVideoButtonSize = (40, 20)

        app.urlSelectVideo = 'https://i.pinimg.com/736x/0f/5c/75/0f5c75e12fa2941a78fa68bd97f4b50c.jpg'

        app.selectVideoButtonLabels = ['Straight Forward', 'Wobbly - Bot', 'Zig - Zag', 'Circle Dance', 'Maze Traversal']

    def drawButton(self, buttonCoords, selectVideoButtonSize, text, labelSize, borderWidth, rectFillColor): #Co-Pilot's idea
        x, y = buttonCoords[0], buttonCoords[1]
        w, h = selectVideoButtonSize[0], selectVideoButtonSize[1]
        drawRect(x, y, w, h, fill=rectFillColor, border='black', borderWidth=borderWidth)
        labelX = x + w / 2
        labelY = y + h / 2
        drawLabel(text, labelX, labelY, fill='black', bold=True, size=labelSize)

    def isPressOnButton(self, buttonCoords, selectVideoButtonSize, mouseX, mouseY): #my own, inspired by Co-Pilot
        x, y = buttonCoords[0], buttonCoords[1]
        width, height = selectVideoButtonSize[0], selectVideoButtonSize[1]
        return x <= mouseX <= x + width and y <= mouseY <= y + height

    def onMousePress(self, app, mouseX, mouseY):
        if self.isPressOnButton(app.straightForwardButtonCoords, app.selectVideoButtonSize, mouseX, mouseY):
            app.selectedExample = app.straightLineRobot
            app.userTypedTitle = app.straightLineRobot
            app.selectedExampleFileName = 'straight'

        elif self.isPressOnButton(app.wobblyBotButtonCoords, app.selectVideoButtonSize, mouseX, mouseY):
            app.selectedExample = app.wobblyRobot
            app.userTypedTitle = app.wobblyRobot
            app.selectedExampleFileName = 'wobble'

        elif self.isPressOnButton(app.zigZagButtonCoords, app.selectVideoButtonSize, mouseX, mouseY):
            app.selectedExample = app.zigZagRobot
            app.userTypedTitle = app.zigZagRobot
            app.selectedExampleFileName = 'zigzag'

        elif self.isPressOnButton(app.circleDanceButtonCoords, app.selectVideoButtonSize, mouseX, mouseY):
            app.selectedExample = app.circleDanceRobot
            app.userTypedTitle = app.circleDanceRobot
            app.selectedExampleFileName = 'circles'

        elif self.isPressOnButton(app.mazeTraversalButtonCoords, app.selectVideoButtonSize, mouseX, mouseY):
            app.selectedExample = app.mazeRobot
            app.userTypedTitle = app.mazeRobot
            app.selectedExampleFileName = 'maze'

        elif self.isPressOnButton(app.selectVideoBackButtonCoords, app.smallSelectVideoButtonSize, mouseX, mouseY):
            return 'Back select video'

        # found that here: "https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory"
        if app.selectedExample is not None:
            dirPath = os.path.dirname(os.path.realpath(__file__))
            app.videoFile = dirPath + "\\..\\videos\\"+app.selectedExampleFileName+".mp4"
            framesLocation = diropenbox(title="Select a folder to store frames")
            app.framesLocation = framesLocation
            if app.videoFile is not None and app.framesLocation is not None:
                app.uploadComplete = True
                extractFrames(app.videoFile, app.framesLocation)
            else:
                app.uploadComplete = False
            print(app.videoFile)


    def redrawAll(self, app):
        drawImage(app.urlSelectVideo, 0, 0)

        drawLabel('Select Sample Video', app.selectVideoScreenTitle[0], app.selectVideoScreenTitle[1], bold=True, fill='darkOrange', font='monospace', size=28)

        self.drawButton(app.straightForwardButtonCoords, app.selectVideoButtonSize, app.selectVideoButtonLabels[0], 22, 5, 'white')
        self.drawButton(app.wobblyBotButtonCoords, app.selectVideoButtonSize, app.selectVideoButtonLabels[1], 22, 5, 'white')
        self.drawButton(app.zigZagButtonCoords, app.selectVideoButtonSize, app.selectVideoButtonLabels[2], 22, 5, 'white')
        self.drawButton(app.circleDanceButtonCoords, app.selectVideoButtonSize, app.selectVideoButtonLabels[3], 22, 5, 'white')
        self.drawButton(app.mazeTraversalButtonCoords, app.selectVideoButtonSize, app.selectVideoButtonLabels[4], 22, 5, 'white')
        self.drawButton(app.selectVideoBackButtonCoords, app.smallSelectVideoButtonSize, 'Back', 12, 3, 'LightGreen')