from cmu_graphics import *
from userFacing import UserFacing
from startScreen import StartScreen
from newProjectScreen import NewProjectScreen
from helpNewProj import HelpNewProj
from helpDraw import HelpDraw
from comparisonResultScreen import ComparisonResultScreen
from comparisonError import ComparisonError
from exampleProjectsStartScreen import ExampleProjectScreen
from selectExampleVideo import SelectExampleVideo
from helpExampleProj import HelpExampleProj
from comparisonExampleError import comparisonExampleError

#shirar's awesome robo project! welcome.

def onAppStart(app):
    app.currentWindow = 'startScreen'

    app.startScreen = StartScreen()
    app.userFacing = UserFacing()
    app.newProjectScreen = NewProjectScreen()
    app.helpNewProj = HelpNewProj()
    app.helpDraw = HelpDraw()
    app.comparisonResultScreen = ComparisonResultScreen()
    app.comparisonError = ComparisonError()
    app.exampleProjectsStartScreen = ExampleProjectScreen()
    app.selectExampleVideo = SelectExampleVideo()
    app.helpExampleProj = HelpExampleProj()
    app.comparisonExampleError = comparisonExampleError()

    app.userFacing.onAppStart(app)
    app.startScreen.onAppStart(app)
    app.newProjectScreen.onAppStart(app)
    app.helpNewProj.onAppStart(app)
    app.helpDraw.onAppStart(app)
    app.comparisonResultScreen.onAppStart(app)
    app.comparisonError.onAppStart(app)
    app.exampleProjectsStartScreen.onAppStart(app)
    app.selectExampleVideo.onAppStart(app)
    app.helpExampleProj.onAppStart(app)
    app.comparisonExampleError.onAppStart(app)

def onKeyPress(app, key):
    if app.currentWindow == 'startScreen':
        app.startScreen.onKeyPress(app, key=key)
    elif app.currentWindow == 'userFacing':
        app.userFacing.onKeyPress(app, key=key)
    elif app.currentWindow == 'newProjectScreen':
        app.newProjectScreen.onKeyPress(app, key=key)
    elif app.currentWindow == 'helpNewProj':
        return
    elif app.currentWindow == 'helpDraw':
        return
    elif app.currentWindow == 'comparisonResultScreen':
        return
    elif app.currentWindow == 'comparisonError':
        return
    elif app.currentWindow == 'exampleProjects':
        app.exampleProjectsStartScreen.onKeyPress(app, key=key)
    elif app.currentWindow == 'selectExampleVideo':
        return
    elif app.currentWindow == 'helpExampleProj':
        return


def onMouseDrag(app, mouseX, mouseY):
    if app.currentWindow == 'startScreen':
        return
    if app.currentWindow == 'newProjectScreen':
        return
    elif app.currentWindow == 'userFacing':
        app.userFacing.onMouseDrag(app, mouseX=mouseX, mouseY=mouseY)
    elif app.currentWindow == 'helpNewProj':
        return
    elif app.currentWindow == 'helpDraw':
        return
    elif app.currentWindow == 'comparisonResultScreen':
        return
    elif app.currentWindow == 'comparisonError':
        return
    elif app.currentWindow == 'exampleProjects':
        return
    elif app.currentWindow == 'selectExampleVideo':
        return
    elif app.currentWindow == 'helpExampleProj':
        return


def onMousePress(app, mouseX, mouseY):
    if app.currentWindow == 'startScreen':
        result = app.startScreen.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'redirect to new Project':
            app.currentWindow = 'newProjectScreen'
        elif result == 'redirect to example projects':
            app.currentWindow = 'exampleProjects'
 
    elif app.currentWindow == 'newProjectScreen':
        result = app.newProjectScreen.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if  result == 'draw':
            app.currentWindow = 'userFacing'
            app.beforeUserFacing = 'newProjectScreen'
        elif result == 'new back':
            app.currentWindow = 'startScreen'
        elif result == 'new help':
            app.currentWindow = 'helpNewProj'
        elif result == 'compare': # and somthing about having all the condtions for drawing and upload complete:
            app.beforeCompare = 'newProjectScreen'
            app.currentWindow = 'comparisonResultScreen'
        elif result == 'new proj error':
            app.currentWindow = 'comparisonError'

    elif app.currentWindow == 'userFacing':
        result = app.userFacing.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'draw back':
            app.currentWindow = app.beforeUserFacing
        elif result == 'draw help':
            app.currentWindow = 'helpDraw'

    elif app.currentWindow == 'helpNewProj':
        result = app.helpNewProj.onMousePress(app, mouseX=mouseX,mouseY=mouseY)
        if result == 'help new proj done':
            app.currentWindow = 'newProjectScreen'

    elif app.currentWindow == 'helpDraw':
        result = app.helpDraw.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'help draw done':
            app.currentWindow = 'userFacing'

    elif app.currentWindow == 'comparisonResultScreen':
        result = app.comparisonResultScreen.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'comparison done':
            app.currentWindow = app.beforeCompare

    elif app.currentWindow == 'comparisonError':
        result = app.comparisonError.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'comparison error done':
            app.currentWindow = 'newProjectScreen'

    elif app.currentWindow == 'exampleProjects':
        result = app.exampleProjectsStartScreen.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'new back':
            app.currentWindow = 'startScreen'
        elif result == 'new help':
            'print example help'
        elif result == 'Select Example Video':
            app.currentWindow = 'selectExampleVideo'
        elif result == 'compare':
            app.currentWindow = 'comparisonResultScreen'
            app.beforeCompare = 'exampleProjects'
        elif result == 'example help':
            app.currentWindow = 'helpExampleProj'
        elif result == 'example back':
            app.currentWindow = 'startScreen'
        elif result == 'example error':
            app.currentWindow = 'comparisonExampleError'

        if result == 'draw':
            app.currentWindow = 'userFacing'
            app.inks.clear()
            app.newStartSquare = None
            app.newEndSquare = None
            app.beforeUserFacing = 'exampleProjects'

    elif app.currentWindow == 'selectExampleVideo':
        app.selectExampleVideo.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        app.currentWindow = 'exampleProjects'
    elif app.currentWindow == 'helpExampleProj':
        result = app.helpExampleProj.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'help Example proj done':
            app.currentWindow = 'exampleProjects'
    elif app.currentWindow == 'comparisonExampleError':
        result = app.comparisonExampleError.onMousePress(app, mouseX=mouseX, mouseY=mouseY)
        if result == 'comparison error example done':
            app.currentWindow = 'exampleProjects'


def onMouseRelease(app, mouseX, mouseY):
    if app.currentWindow == 'startScreen':
        return
    elif app.currentWindow == 'newProjectScreen':
        return
    elif app.currentWindow == 'userFacing':
        app.userFacing.onMouseRelease(app, mouseX=mouseX, mouseY=mouseY)
    elif app.currentWindow == 'helpNewProj':
        return
    elif app.currentWindow == 'helpDraw':
        return
    elif app.currentWindow == 'comparisonResultScreen':
        return
    elif app.currentWindow == 'comparisonError':
        return
    elif app.currentWindow == 'exampleProjects':
        return
    elif app.currentWindow == 'selectExampleVideo':
        return
    elif app.currentWindow == 'helpExampleProj':
        return


def redrawAll(app):
    if app.currentWindow == 'startScreen':
        app.startScreen.redrawAll(app)
    elif app.currentWindow == 'newProjectScreen':
        app.newProjectScreen.redrawAll(app)
    elif app.currentWindow == 'userFacing':
        app.userFacing.redrawAll(app)
    elif app.currentWindow == 'helpNewProj':
        app.helpNewProj.redrawAll(app)
    elif app.currentWindow == 'helpDraw':
        app.helpDraw.redrawAll(app)
    elif app.currentWindow == 'comparisonResultScreen':
        app.comparisonResultScreen.redrawAll(app)
    elif app.currentWindow == 'comparisonError':
        app.comparisonError.redrawAll(app)
    elif app.currentWindow == 'exampleProjects':
        app.exampleProjectsStartScreen.redrawAll(app)
    elif app.currentWindow == 'selectExampleVideo':
        app.selectExampleVideo.redrawAll(app)
    elif app.currentWindow == 'helpExampleProj':
        app.helpExampleProj.redrawAll(app)
    elif app.currentWindow == 'comparisonExampleError':
        app.comparisonExampleError.redrawAll(app)


def main():
    runApp()

main()
