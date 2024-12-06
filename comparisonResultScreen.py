from cmu_graphics import *
from robotPath import percentAccuracy
from userFacing import *

class ComparisonResultScreen:
    def onAppStart(self, app):
        app.urlcomparison = 'https://i.pinimg.com/736x/7a/94/b9/7a94b99692fd54526b7de70e2f05e31f.jpg'

        app.comparisonTitle = (200, 60)
        app.titleOfProjectCoords = (200, 90)
        app.comparisonText1 = (200, 120)


        app.smallLineSpacing = 25

        app.comparisonPopUpCoords = (30, 30)
        app.comparisonPopUpSize = (340, 340)

        app.comparisonDoneButtonCoords = (235, 330)
        app.comparisonDoneButtonSize = (70, 25)

        app.comparisonRobotPathCoords = (80, 330)
        app.comparisonRobotPathSize = (70, 25)

        app.listOfColors = [app.color1, app.color2, app.color3, app.color4, app.color5, app.color6, app.color7]
        app.listOfPercentDistribution = ['0% - 9.9%', '10% - 29.9%', '30% - 49.9%', '50% - 69.9%', '70% - 89.9%',
                                         '90% - 99.9%', '100%']

        app.squaresOfColorStartCoords = (85, 180)
        app.squaresOfColorSize = (60, 16)
        app.percentDistributionStartCoords = (270, 188)
        app.colorSpacing = 20

    def onMousePress(self, app, mouseX, mouseY):
        if (app.comparisonDoneButtonCoords[0] <= mouseX <= app.comparisonDoneButtonCoords[0] + app.comparisonDoneButtonSize[
            0] and
                app.comparisonDoneButtonCoords[1] <= mouseY <= app.comparisonDoneButtonCoords[1] +
                app.comparisonDoneButtonSize[1]):
            return 'comparison done'

        if (app.comparisonRobotPathCoords[0] <= mouseX <= app.comparisonRobotPathCoords[0] +
                app.comparisonRobotPathSize[0] and
                app.comparisonRobotPathCoords[1] <= mouseY <= app.comparisonRobotPathCoords[1] +
                app.comparisonRobotPathSize[1]):
            app.image.show()
            return 'picture pop up'

    def redrawAll(self, app):
        # Background
        drawImage(app.urlcomparison, 0, 0)

        # Instructions
        drawRect(app.comparisonPopUpCoords[0], app.comparisonPopUpCoords[1], app.comparisonPopUpSize[0],
                 app.comparisonPopUpSize[1], fill='white', border='black', borderWidth=1)

        # Page Title
        drawLabel('Comparison Results', app.comparisonTitle[0], app.comparisonTitle[1], fill='deepPink', bold=True,
                  font='monospace', size=24)

        # Project Title
        if len(app.userTypedTitle) == 0:
            drawLabel('[NO PROJECT TITLE]', app.titleOfProjectCoords[0], app.titleOfProjectCoords[1], size = 20, fill = 'Grey')
        elif len(app.userTypedTitle) >= 0 :
            drawLabel(f'{app.userTypedTitle}', app.titleOfProjectCoords[0], app.titleOfProjectCoords[1], size = 20, fill = 'mediumVioletRed')

        # Text
        drawLabel('Your Score:', app.comparisonText1[0], app.comparisonText1[1], size=18, bold=True)
        drawLabel(f'{app.number}%', app.comparisonText1[0], (app.comparisonText1[1] + (app.smallLineSpacing * 1)),
                  fill=app.colorScore, bold=True, border='Black', size=40)
        drawLabel('accurate', app.comparisonText1[0], (app.comparisonText1[1] + (app.smallLineSpacing * 2)), size=14)

        # Squares of Color
        for i in range(len(app.listOfColors)):
            drawRect(app.squaresOfColorStartCoords[0], app.squaresOfColorStartCoords[1] + i * (app.colorSpacing),
                     app.squaresOfColorSize[0], app.squaresOfColorSize[1], fill=app.listOfColors[i], border='black')

        for j in range(len(app.listOfPercentDistribution)):
            drawLabel(app.listOfPercentDistribution[j], app.percentDistributionStartCoords[0],
                      app.percentDistributionStartCoords[1] + j * (app.colorSpacing),
                      fill=app.listOfColors[j], size=14)

        #print(percentAccuracy(app.newStartSquare, app.startSquareDiment, app.newEndSquare, app.endSquareDiment, app.inks)) # uses thing
        #from the robot path to find the percent, but not sure if this is right

        # Done button
        drawRect(app.comparisonDoneButtonCoords[0], app.comparisonDoneButtonCoords[1], app.comparisonDoneButtonSize[0],
                 app.comparisonDoneButtonSize[1], fill='lightGreen', border='black', borderWidth=3)
        backButtonLabelX = app.comparisonDoneButtonCoords[0] + app.comparisonDoneButtonSize[0] / 2
        backButtonLabelY = app.comparisonDoneButtonCoords[1] + app.comparisonDoneButtonSize[1] / 2
        drawLabel('Done', backButtonLabelX, backButtonLabelY, fill='black', bold=True, size=14)

        # Image button
        drawRect(app.comparisonRobotPathCoords[0], app.comparisonRobotPathCoords[1], app.comparisonRobotPathSize[0],
                 app.comparisonRobotPathSize[1], fill='Gold', border='black', borderWidth=3)
        robotButtonLabelX = app.comparisonRobotPathCoords[0] + app.comparisonRobotPathSize[0] / 2
        robotButtonLabelY = app.comparisonRobotPathCoords[1] + app.comparisonRobotPathSize[1] / 2
        drawLabel('See Image', robotButtonLabelX, robotButtonLabelY, fill='black', bold=True, size=12)

