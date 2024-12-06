from cmu_graphics import *

class comparisonExampleError:
    def onAppStart(self, app):
        app.urlcomparisonExampleError = 'https://i.pinimg.com/736x/0c/40/3b/0c403bf05f0849256f661a604b45ffc6.jpg'

        app.comparisonExampleErrorTitle = (200, 60)
        app.comparisonExampleErrorText1 = (200, 120)
        app.comparisonExampleErrorText2 = (200, 150)
        app.comparisonExampleErrorText3 = (200, 230)

        app.smallLineSpacingError = 16

        app.comparisonExampleErrorPopUpCoords = (30, 30)
        app.comparisonExampleErrorPopUpSize = (340, 340)

        app.comparisonExampleErrorDoneButtonCoords = (165, 330)
        app.comparisonExampleErrorDoneButtonSize = (70, 25)

        app.uploadComplete = False
        app.isDrawingComplete = False

    def onMousePress(self, app, mouseX, mouseY):
        if (app.comparisonExampleErrorDoneButtonCoords[0] <= mouseX <= app.comparisonExampleErrorDoneButtonCoords[0] +
                app.comparisonExampleErrorDoneButtonSize[0] and
                app.comparisonExampleErrorDoneButtonCoords[1] <= mouseY <= app.comparisonExampleErrorDoneButtonCoords[1] +
                app.comparisonExampleErrorDoneButtonSize[1]):
            return 'comparison error example done'

    def redrawAll(self, app):
        # Background
        drawImage(app.urlcomparisonExampleError, 0, 0)

        # Instructions
        drawRect(app.comparisonExampleErrorPopUpCoords[0], app.comparisonExampleErrorPopUpCoords[1], app.comparisonExampleErrorPopUpSize[0],
                 app.comparisonExampleErrorPopUpSize[1],
                 fill='white', border='Darkred', borderWidth=5)

        # Title
        drawLabel('ERROR: Missing', app.comparisonExampleErrorTitle[0], app.comparisonExampleErrorTitle[1], fill='red', bold=True,
                  font='monospace', size=24)

        # Text
        drawLabel('Your are missing one of the following:', app.comparisonExampleErrorText1[0], app.comparisonExampleErrorText1[1],
                  fill='darkred', size=16, bold=True)

        # File Upload Section
        if app.uploadComplete:
            drawLabel('[COMPLETE] Selected Video', app.comparisonExampleErrorText2[0], app.comparisonExampleErrorText2[1], size=16,
                      bold=True, fill='green')
            drawLabel('Awesome!', app.comparisonExampleErrorText2[0],
                      app.comparisonExampleErrorText2[1] + app.smallLineSpacingError * 1, size=16)
        else:
            drawLabel('[MISSING] Selected Video', app.comparisonExampleErrorText2[0], app.comparisonExampleErrorText2[1], size=16,
                      bold=True, fill='red')
            drawLabel('Please select the example video AND', app.comparisonExampleErrorText2[0],
                      app.comparisonExampleErrorText2[1] + app.smallLineSpacingError * 1, size=16)
            drawLabel('select a temporary place on your device', app.comparisonExampleErrorText2[0],
                      app.comparisonExampleErrorText2[1] + app.smallLineSpacingError * 2, size=16)
            drawLabel('to store the frames from the video.', app.comparisonExampleErrorText2[0],
                      app.comparisonExampleErrorText2[1] + app.smallLineSpacingError * 3, size=16)

        # Drawing of Correct Path Section
        if app.isDrawingComplete:
            drawLabel('[COMPLETE] Drawing of Correct Path', app.comparisonExampleErrorText3[0], app.comparisonExampleErrorText3[1],
                      size=16, bold=True, fill='green')
            drawLabel('Great Job!', app.comparisonExampleErrorText3[0],
                      app.comparisonExampleErrorText3[1] + app.smallLineSpacingError * 1, size=16)
        else:
            drawLabel('[MISSING] Drawing of Correct Path', app.comparisonExampleErrorText3[0], app.comparisonExampleErrorText3[1],
                      size=16, bold=True, fill='red')
            drawLabel('Draw the path for the robot. Make sure both', app.comparisonExampleErrorText3[0],
                      app.comparisonExampleErrorText3[1] + app.smallLineSpacingError * 1, size=16)
            drawLabel('the start and end squares are fixed, and', app.comparisonExampleErrorText3[0],
                      app.comparisonExampleErrorText3[1] + app.smallLineSpacingError * 2, size=16)
            drawLabel('there is a drawn path connecting the two.', app.comparisonExampleErrorText3[0],
                      app.comparisonExampleErrorText3[1] + app.smallLineSpacingError * 3, size=16)

        # Done button
        drawRect(app.comparisonExampleErrorDoneButtonCoords[0], app.comparisonExampleErrorDoneButtonCoords[1],
                 app.comparisonExampleErrorDoneButtonSize[0],
                 app.comparisonExampleErrorDoneButtonSize[1], fill='lightGreen', border='black', borderWidth=3)
        backButtonLabelX = app.comparisonExampleErrorDoneButtonCoords[0] + app.comparisonExampleErrorDoneButtonSize[0] / 2
        backButtonLabelY = app.comparisonExampleErrorDoneButtonCoords[1] + app.comparisonExampleErrorDoneButtonSize[1] / 2
        drawLabel('Done', backButtonLabelX, backButtonLabelY, fill='black', bold=True, size=14)