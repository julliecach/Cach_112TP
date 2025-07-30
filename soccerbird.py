from cmu_graphics import *
import random
import math

def onAppStart(app):
    app.rectW = app.width
    app.rectH = app.height
    
    #Icon (bird) coordinates and variables
    app.iconX, app.iconY = 50, app.height/2
    app.iconStepsPerSecond = 1
    app.isPaused = True
    
    #Game Intial
    app.isGameStart = False
    
    
    
##########################################################################
                # Intial isntructions/ before game
##########################################################################
def instructions_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'lightblue')
    drawLabel('Welcome to Messi Bird!', 200, 50, fill = 'black', size = 36)
    drawLabel('How To Play:', 200, 100, fill = 'black', size = 24)
    drawLabel('1). To begin game, click on return/enter key', 150, 150, 
              fill = 'black')
    drawLabel('2). To move Messi, click on the space button.', 155, 165, 
              fill = 'black')
    drawLabel("This will make Messi jump inorder to move through the pillars", 
                215, 180, fill = 'black')
    drawLabel('3). Hitting the pillars = GAME OVER', 132, 195, fill = 'black')
    
    drawLabel('**Note: score is increased each time you pass a pillar!', 200, 
                220, fill = 'black')
    drawLabel('Click SPACE to move to game screen!', 200, 250, fill = 'black')
                
def instructions_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('start')





##############################################################################
                # when Game has begun 
#############################################################################
def start_redrawAll(app):
## initial background soccer field
    drawRect(0, 0, app.rectW, app.rectH, fill = 'green', opacity = 90 )
    drawLine(app.width/2, 0, 200, app.height, fill = 'white')
    # right goal area
    drawLine(0, 150, 50, 150, fill = 'white')
    drawLine(50, 150, 50, 250, fill = 'white')
    drawLine(0, 250, 50, 250, fill = 'white')
    #left goal area
    drawLine(app.width - 50, 150, app.width, 150, fill = 'white')
    drawLine(app.width - 50, 150, app.width - 50, 250, fill = 'white')
    drawLine(app.width - 50, 250, app.width, 250, fill = 'white')
    
    # pillars to jump through
    drawPillars(app)
    
    #Bird icon (circle is temporary)
    drawIcon(app)
    
def drawPillars(app):
    #top pillars
    for i in range(5):
        x0 = (60 * i) + 120
        drawRect(x0, 0, 30, 170, fill = 'pink', border = 'black')
    #bottom pillars
    for j in range(5):
        x0 = (60 *j) + 120
        drawRect(x0, 270, 30, app.height, fill = 'pink', border = 'black')
      
def drawIcon(app):
    drawCircle(app.iconX, app.iconY, 20, fill = 'lightblue', border = 'black')
    
# Moving the bird section:
def start_onKeyPress(app, key):
    if key == 'enter':
        app.isGameStart = True
        start_onStep(app)
    if app.isGameStart:
        if key == 'space':
            app.iconX += 20
            app.iconY -= 15

def start_onStep(app):
    if app.isGameStart:
        app.iconY += app.iconStepsPerSecond
        

    
#def takeStep(app):
   # app.iconX += app.iconStepsPerSecond
   




# Game Button to start

class Button:
    def __init__(self):
        pass
    
   

def main():
    runAppWithScreens(initialScreen = 'instructions')

main()

cmu_graphics.run()

