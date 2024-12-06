from cmu_graphics import *

class StartScreen:
    def onAppStart(self, app):
        app.roboTitleCoords = (140, 50)
        app.graderTitleCoords = (230, 120)

        app.highlight1Coords = (40, 175)
        app.highlightSize = (320, 70)

        app.newProjButtonCoords = (50, 185)
        app.newProjTextCoords = (200, 210)
        app.startHereSuggestionCoords = (70, 175)

        app.buttonSize = (300, 60)

        app.exampleProjectButtonCoords = (50, 265)
        app.exampleProjectTextCoords = (200, 290)

        app.bigButtonSize = (320, 80)
        app.url = 'https://i.pinimg.com/736x/2d/bf/8c/2dbf8c73b9bdfa8244d37f65d6260cbf.jpg'

    def onMousePress(self, app, mouseX, mouseY):
        if (app.newProjButtonCoords[0] <= mouseX <= app.newProjButtonCoords[0] + app.buttonSize[0] and
                app.newProjButtonCoords[1] <= mouseY <= app.newProjButtonCoords[1] + app.buttonSize[1]):
            return 'redirect to new Project'

        if (app.exampleProjectButtonCoords[0] <= mouseX <= app.exampleProjectButtonCoords[0] + app.buttonSize[0] and
                app.exampleProjectButtonCoords[1] <= mouseY <= app.exampleProjectButtonCoords[1] + app.buttonSize[1]):
            return 'redirect to example projects'
        return False

    def redrawAll(self, app):
        drawImage(app.url, 0, 0)

        drawLabel('ROBO-', app.roboTitleCoords[0], app.roboTitleCoords[1], bold=True, fill='navy', font='monospace',
                  size=80)
        drawLabel('GRADER', app.graderTitleCoords[0], app.graderTitleCoords[1], bold=True, fill='navy',
                  font='monospace',
                  size=80)

        #new project
        drawRect(app.highlight1Coords[0], app.highlight1Coords[1], app.highlightSize[0], app.highlightSize[1],
                 fill='yellow', opacity=50)
        drawRect(app.newProjButtonCoords[0], app.newProjButtonCoords[1], app.buttonSize[0], app.buttonSize[1],
                 fill='white',
                 border='black', borderWidth=5)

        #example projects
        drawRect(app.exampleProjectButtonCoords[0], app.exampleProjectButtonCoords[1], app.buttonSize[0], app.buttonSize[1],
                 fill='white', border='black', borderWidth=5)

        drawLabel('Start here!', app.startHereSuggestionCoords[0], app.startHereSuggestionCoords[1], fill='red', bold=True, size=14)
        drawLabel('New Project', app.newProjTextCoords[0], app.newProjTextCoords[1], fill='black', bold=True, size=26)
        drawLabel('Example Projects', app.exampleProjectTextCoords[0], app.exampleProjectTextCoords[1], fill='black', bold=True, size=26)