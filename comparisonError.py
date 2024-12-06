from cmu_graphics import *

class ComparisonError:
    def onAppStart(self, app):
        app.urlcomparisonError = 'https://i.pinimg.com/736x/96/9c/21/969c215f04ad0800c5cfcab37b8cf945.jpg'

        app.comparisonErrorTitle = (200, 60)
        app.comparisonErrorText1 = (200, 120)
        app.comparisonErrorText2 = (200, 150)
        app.comparisonErrorText3 = (200, 230)

        app.smallLineSpacingError = 16

        app.comparisonErrorPopUpCoords = (30, 30)
        app.comparisonErrorPopUpSize = (340, 340)

        app.comparisonErrorDoneButtonCoords = (165, 330)
        app.comparisonErrorDoneButtonSize = (70, 25)

        app.uploadComplete = False
        app.isDrawingComplete = True

    def onMousePress(self, app, mouseX, mouseY):
        if (app.comparisonErrorDoneButtonCoords[0] <= mouseX <= app.comparisonErrorDoneButtonCoords[0] +
                app.comparisonErrorDoneButtonSize[0] and
                app.comparisonErrorDoneButtonCoords[1] <= mouseY <= app.comparisonErrorDoneButtonCoords[1] +
                app.comparisonErrorDoneButtonSize[1]):
            return 'comparison error done'

    def redrawAll(self, app):
        # Background
        drawImage(app.urlcomparisonError, 0, 0)

        # Instructions
        drawRect(app.comparisonErrorPopUpCoords[0], app.comparisonErrorPopUpCoords[1], app.comparisonErrorPopUpSize[0],
                 app.comparisonErrorPopUpSize[1],
                 fill='white', border='Darkred', borderWidth=5)

        # Title
        drawLabel('ERROR: Missing', app.comparisonErrorTitle[0], app.comparisonErrorTitle[1], fill='red', bold=True,
                  font='monospace', size=24)

        # Text
        drawLabel('Your are missing one of the following:', app.comparisonErrorText1[0], app.comparisonErrorText1[1],
                  fill='darkred', size=16, bold=True)

        # File Upload Section
        if app.uploadComplete:
            drawLabel('[COMPLETE] File Upload', app.comparisonErrorText2[0], app.comparisonErrorText2[1], size=16,
                      bold=True, fill='green')
            drawLabel('Awesome!', app.comparisonErrorText2[0],
                      app.comparisonErrorText2[1] + app.smallLineSpacingError * 1, size=16)
        else:
            drawLabel('[MISSING] File Upload', app.comparisonErrorText2[0], app.comparisonErrorText2[1], size=16,
                      bold=True, fill='red')
            drawLabel('Please upload the correct video file AND', app.comparisonErrorText2[0],
                      app.comparisonErrorText2[1] + app.smallLineSpacingError * 1, size=16)
            drawLabel('select a temporary place on your device', app.comparisonErrorText2[0],
                      app.comparisonErrorText2[1] + app.smallLineSpacingError * 2, size=16)
            drawLabel('to store the frames from the video.', app.comparisonErrorText2[0],
                      app.comparisonErrorText2[1] + app.smallLineSpacingError * 3, size=16)

        # Drawing of Correct Path Section
        if app.isDrawingComplete:
            drawLabel('[COMPLETE] Drawing of Correct Path', app.comparisonErrorText3[0], app.comparisonErrorText3[1],
                      size=16, bold=True, fill='green')
            drawLabel('Great Job!', app.comparisonErrorText3[0],
                      app.comparisonErrorText3[1] + app.smallLineSpacingError * 1, size=16)
        else:
            drawLabel('[MISSING] Drawing of Correct Path', app.comparisonErrorText3[0], app.comparisonErrorText3[1],
                      size=16, bold=True, fill='red')
            drawLabel('Draw the path for the robot. Make sure both', app.comparisonErrorText3[0],
                      app.comparisonErrorText3[1] + app.smallLineSpacingError * 1, size=16)
            drawLabel('the start and end squares are fixed, and', app.comparisonErrorText3[0],
                      app.comparisonErrorText3[1] + app.smallLineSpacingError * 2, size=16)
            drawLabel('there is a drawn path connecting the two.', app.comparisonErrorText3[0],
                      app.comparisonErrorText3[1] + app.smallLineSpacingError * 3, size=16)

        # Done button
        drawRect(app.comparisonErrorDoneButtonCoords[0], app.comparisonErrorDoneButtonCoords[1],
                 app.comparisonErrorDoneButtonSize[0],
                 app.comparisonErrorDoneButtonSize[1], fill='lightGreen', border='black', borderWidth=3)
        backButtonLabelX = app.comparisonErrorDoneButtonCoords[0] + app.comparisonErrorDoneButtonSize[0] / 2
        backButtonLabelY = app.comparisonErrorDoneButtonCoords[1] + app.comparisonErrorDoneButtonSize[1] / 2
        drawLabel('Done', backButtonLabelX, backButtonLabelY, fill='black', bold=True, size=14)