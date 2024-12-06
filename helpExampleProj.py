from cmu_graphics import *

class HelpExampleProj:
    def onAppStart(self, app):
        app.urlHelpExampleProj = 'https://i.pinimg.com/736x/22/36/f4/2236f44a5c88de90871c9339d1146c28.jpg' #i made this

        app.helpExampleProjTitle = (200, 60)
        app.helpExampleProjText1 = (200, 90)
        app.helpExampleProjText2 = (200, 155)
        app.helpExampleProjText3 = (200, 205)

        app.ExampleProjSmallLineSpacing = 16

        app.helpExampleProjPopUpCoords = (30, 30)
        app.helpExampleProjPopUpSize = (340, 340)

        app.helpExampleProjDoneButtonCoords = (165, 330)
        app.helpExampleProjDoneButtonSize = (70, 25)


    def onMousePress(self, app, mouseX, mouseY):
        if (app.helpExampleProjDoneButtonCoords[0] <= mouseX <= app.helpExampleProjDoneButtonCoords[0] +
                app.helpExampleProjDoneButtonSize[0] and
                app.helpExampleProjDoneButtonCoords[1] <= mouseY <= app.helpExampleProjDoneButtonCoords[1] +
                app.helpExampleProjDoneButtonSize[1]):
            return 'help Example proj done'


    def redrawAll(self, app):
        # Background
        drawImage(app.urlHelpExampleProj, 0, 0)

        # Instructions
        drawRect(app.helpExampleProjPopUpCoords[0], app.helpExampleProjPopUpCoords[1], app.helpExampleProjPopUpSize[0],
                 app.helpExampleProjPopUpSize[1], fill='white', border='black', borderWidth=5)

        # Title
        drawLabel('Instructions', app.helpExampleProjTitle[0], app.helpExampleProjTitle[1], bold=True, font='monospace',
                  size=24)

        # Text
        drawLabel('1. Select Project', app.helpExampleProjText1[0], app.helpExampleProjText1[1], size=16, bold=True)
        drawLabel('Click to pick a video file out of the', app.helpExampleProjText1[0],
                  app.helpExampleProjText1[1] + (app.ExampleProjSmallLineSpacing * 1), size=16)
        drawLabel('options. Patiently wait until it loads!', app.helpExampleProjText1[0],
                  app.helpExampleProjText1[1] + (app.ExampleProjSmallLineSpacing * 2), size=16)

        drawLabel('2. Draw Ideal Path', app.helpExampleProjText2[0], app.helpExampleProjText2[1], size=16, bold=True)
        drawLabel('Draw the intended path of the robot.', app.helpExampleProjText2[0],
                  app.helpExampleProjText2[1] + (app.ExampleProjSmallLineSpacing * 1), size=16)

        drawLabel('3. Compare Paths', app.helpExampleProjText3[0], app.helpExampleProjText3[1], size=16, bold=True)
        drawLabel('Compare the path the robot took against', app.helpExampleProjText3[0],
                  app.helpExampleProjText3[1] + (app.ExampleProjSmallLineSpacing * 1), size=16)
        drawLabel('the intended path you drew for it!', app.helpExampleProjText3[0],
                  app.helpExampleProjText3[1] + (app.ExampleProjSmallLineSpacing * 2), size=16)

        # Done button
        drawRect(app.helpExampleProjDoneButtonCoords[0], app.helpExampleProjDoneButtonCoords[1], app.helpExampleProjDoneButtonSize[0],
                 app.helpExampleProjDoneButtonSize[1], fill='LightGreen',
                 border='black', borderWidth=3)
        backButtonExampleProjLabelX = app.helpExampleProjDoneButtonCoords[0] + app.helpExampleProjDoneButtonSize[0] / 2
        backButtonExampleProjLabelY = app.helpExampleProjDoneButtonCoords[1] + app.helpExampleProjDoneButtonSize[1] / 2
        drawLabel('Done', backButtonExampleProjLabelX, backButtonExampleProjLabelY, fill='black', bold=True, size=14)
