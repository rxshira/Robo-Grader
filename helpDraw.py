from cmu_graphics import *

class HelpDraw:
    def onAppStart(self, app):
        app.urlHelpDraw = 'https://i.pinimg.com/736x/be/b4/ff/beb4ff256416f60b5673c1f93d007932.jpg'

        app.helpDrawTitle = (200, 60)
        app.helpDrawText1 = (200, 90)
        app.helpDrawText2 = (200, 170)
        app.helpDrawText3 = (200, 250)

        app.smallLineSpacingHelpDraw = 16

        app.helpDrawPopUpCoords = (30, 30)
        app.helpDrawPopUpSize = (340, 340)

        app.helpDrawDoneButtonCoords = (165, 330)
        app.helpDrawDoneButtonSize = (70, 25)


    def onMousePress(self, app, mouseX, mouseY):
        if (app.helpDrawDoneButtonCoords[0] <= mouseX <= app.helpDrawDoneButtonCoords[0] + app.helpDrawDoneButtonSize[0] and
                app.helpDrawDoneButtonCoords[1] <= mouseY <= app.helpDrawDoneButtonCoords[1] + app.helpDrawDoneButtonSize[1]):
            return 'help draw done'

    def redrawAll(self, app):
        # Background
        drawImage(app.urlHelpDraw, 0, 0)

        # Instructions
        drawRect(app.helpDrawPopUpCoords[0], app.helpDrawPopUpCoords[1], app.helpDrawPopUpSize[0], app.helpDrawPopUpSize[1],
                 fill='white', border='black', borderWidth=5)

        # Title
        drawLabel('Draw - Instructions', app.helpDrawTitle[0], app.helpDrawTitle[1], bold=True, font='monospace',
                  size=24)

        # Text
        drawLabel('1. Red and Green Squares', app.helpDrawText1[0], app.helpDrawText1[1], size=16, bold=True)
        drawLabel('Click the squares, then move them in', app.helpDrawText1[0],
                  app.helpDrawText1[1] + (app.smallLineSpacingHelpDraw * 1), size=16)
        drawLabel('the canvas. Red is for where the robot starts', app.helpDrawText1[0],
                  app.helpDrawText1[1] + (app.smallLineSpacingHelpDraw * 2), size=16)
        drawLabel('and green is the fixed end goal.', app.helpDrawText1[0],
                  app.helpDrawText1[1] + (app.smallLineSpacingHelpDraw * 3), size=16)

        drawLabel('2. Fix/Unfix Buttons', app.helpDrawText2[0], app.helpDrawText2[1], size=16, bold=True)
        drawLabel('Once you set the squares in place, click the', app.helpDrawText2[0],
                  app.helpDrawText2[1] + (app.smallLineSpacingHelpDraw * 1), size=16)
        drawLabel('fix button. When a square is fixed, it will not', app.helpDrawText2[0],
                  app.helpDrawText2[1] + (app.smallLineSpacingHelpDraw * 2), size=16)
        drawLabel('move. Click the unfix button to let it move.', app.helpDrawText2[0],
                  app.helpDrawText2[1] + (app.smallLineSpacingHelpDraw * 3), size=16)

        drawLabel('3. Draw and Clear Buttons', app.helpDrawText3[0], app.helpDrawText3[1], size=16, bold=True)
        drawLabel('Draw the path for the robot. If the line does', app.helpDrawText3[0],
                  app.helpDrawText3[1] + (app.smallLineSpacingHelpDraw * 1), size=16)
        drawLabel('not start at red and end at green, it will auto-', app.helpDrawText3[0],
                  app.helpDrawText3[1] + (app.smallLineSpacingHelpDraw * 2), size=16)
        drawLabel('-delete. Click Clear to clear the canvas.', app.helpDrawText3[0],
                  app.helpDrawText3[1] + (app.smallLineSpacingHelpDraw * 3), size=16)

        # Done button
        drawRect(app.helpDrawDoneButtonCoords[0], app.helpDrawDoneButtonCoords[1], app.helpDrawDoneButtonSize[0],
                 app.helpDrawDoneButtonSize[1], fill='lightGreen',
                 border='black', borderWidth=3)
        backButtonLabelX = app.helpDrawDoneButtonCoords[0] + app.helpDrawDoneButtonSize[0] / 2
        backButtonLabelY = app.helpDrawDoneButtonCoords[1] + app.helpDrawDoneButtonSize[1] / 2
        drawLabel('Done', backButtonLabelX, backButtonLabelY, fill='black', bold=True, size=14)