from cmu_graphics import *

class HelpNewProj:
    def onAppStart(self, app):
        app.urlHelpNewProj = 'https://i.pinimg.com/736x/13/8c/15/138c150d9d3722abd73a88319fcc3219.jpg' #i made this

        app.helpNewProjTitle = (200, 60)
        app.helpNewProjText1 = (200, 90)
        app.helpNewProjText2 = (200, 155)
        app.helpNewProjText3 = (200, 220)
        app.helpNewProjText4 = (200, 270)

        app.newProjSmallLineSpacing = 16

        app.helpNewProjPopUpCoords = (30, 30)
        app.helpNewProjPopUpSize = (340, 340)

        app.helpNewProjDoneButtonCoords = (165, 330)
        app.helpNewProjDoneButtonSize = (70, 25)


    def onMousePress(self, app, mouseX, mouseY):
        if (app.helpNewProjDoneButtonCoords[0] <= mouseX <= app.helpNewProjDoneButtonCoords[0] +
                app.helpNewProjDoneButtonSize[0] and
                app.helpNewProjDoneButtonCoords[1] <= mouseY <= app.helpNewProjDoneButtonCoords[1] +
                app.helpNewProjDoneButtonSize[1]):
            return 'help new proj done'


    def redrawAll(self, app):
        # Background
        drawImage(app.urlHelpNewProj, 0, 0)

        # Instructions
        drawRect(app.helpNewProjPopUpCoords[0], app.helpNewProjPopUpCoords[1], app.helpNewProjPopUpSize[0],
                 app.helpNewProjPopUpSize[1], fill='white', border='black', borderWidth=5)

        # Title
        drawLabel('Instructions', app.helpNewProjTitle[0], app.helpNewProjTitle[1], bold=True, font='monospace',
                  size=24)

        # Text
        drawLabel('1. Title', app.helpNewProjText1[0], app.helpNewProjText1[1], size=16, bold=True)
        drawLabel('Click above the line, type the title. Use only', app.helpNewProjText1[0],
                  app.helpNewProjText1[1] + (app.newProjSmallLineSpacing * 1), size=16)
        drawLabel('Letters/Numbers. 14 characters max.', app.helpNewProjText1[0],
                  app.helpNewProjText1[1] + (app.newProjSmallLineSpacing * 2), size=16)

        drawLabel('2. Upload Files', app.helpNewProjText2[0], app.helpNewProjText2[1], size=16, bold=True)
        drawLabel('Click to pick a video file. It must include', app.helpNewProjText2[0],
                  app.helpNewProjText2[1] + (app.newProjSmallLineSpacing * 1), size=16)
        drawLabel('the moving blue and target green area.', app.helpNewProjText2[0],
                  app.helpNewProjText2[1] + (app.newProjSmallLineSpacing * 2), size=16)

        drawLabel('3. Draw Ideal Path', app.helpNewProjText3[0], app.helpNewProjText3[1], size=16, bold=True)
        drawLabel('Draw the intended path of the robot.', app.helpNewProjText3[0],
                  app.helpNewProjText3[1] + (app.newProjSmallLineSpacing * 1), size=16)

        drawLabel('4. Compare Paths', app.helpNewProjText4[0], app.helpNewProjText4[1], size=16, bold=True)
        drawLabel('Compare the path the robot took against', app.helpNewProjText4[0],
                  app.helpNewProjText4[1] + (app.newProjSmallLineSpacing * 1), size=16)
        drawLabel('the intended path you drew for it!', app.helpNewProjText4[0],
                  app.helpNewProjText4[1] + (app.newProjSmallLineSpacing * 2), size=16)

        # Done button
        drawRect(app.helpNewProjDoneButtonCoords[0], app.helpNewProjDoneButtonCoords[1], app.helpNewProjDoneButtonSize[0],
                 app.helpNewProjDoneButtonSize[1], fill='lightGreen',
                 border='black', borderWidth=3)
        backButtonNewProjLabelX = app.helpNewProjDoneButtonCoords[0] + app.helpNewProjDoneButtonSize[0] / 2
        backButtonNewProjLabelY = app.helpNewProjDoneButtonCoords[1] + app.helpNewProjDoneButtonSize[1] / 2
        drawLabel('Done', backButtonNewProjLabelX, backButtonNewProjLabelY, fill='black', bold=True, size=14)
